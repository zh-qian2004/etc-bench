#!/usr/bin/env python3
"""Evaluate ETC predictions with SENA."""
from __future__ import annotations

import argparse
import importlib.machinery
import json
import os
import sys
import types
from collections import defaultdict
from pathlib import Path

os.environ.setdefault("TORCH_DEVICE_BACKEND_AUTOLOAD", "0")

import torch

try:  # Use the real backend when CANN is configured.
    import torch_npu  # noqa: F401
except Exception:  # pragma: no cover - optional backend is unusable
    sys.modules.pop("torch_npu", None)
    mock_npu = types.ModuleType("torch_npu")
    mock_npu.__path__ = []
    mock_npu.__spec__ = importlib.machinery.ModuleSpec("torch_npu", None)
    mock_npu.npu = types.ModuleType("torch_npu.npu")
    mock_npu.npu.__spec__ = importlib.machinery.ModuleSpec("torch_npu.npu", None)
    sys.modules["torch_npu"] = mock_npu
    sys.modules["torch_npu.npu"] = mock_npu.npu

from bert_score import BERTScorer

from validate_predictions import load_jsonl, validate


REPOSITORY = Path(__file__).resolve().parents[1]
DEFAULT_BENCHMARK = REPOSITORY / "benchmark"
DEFAULT_ENCODER = "xlm-roberta-large"


def score_f1(scorer: BERTScorer, candidates: list[str], references: list[str]) -> list[float]:
    _, _, f1 = scorer.score(candidates, references)
    return [float(value) for value in f1]


def new_tally() -> dict:
    return {"total": 0, "exact": 0, "semantic": 0, "joint": 0}


def add(tally: dict, exact: bool, semantic: bool, joint: bool) -> None:
    tally["total"] += 1
    tally["exact"] += int(exact)
    tally["semantic"] += int(semantic)
    tally["joint"] += int(joint)


def finish(tally: dict) -> dict:
    total = tally["total"]
    return {
        **tally,
        "exact_match_pct": round(100 * tally["exact"] / total, 2) if total else 0.0,
        "semantic_preservation_pct": round(100 * tally["semantic"] / total, 2) if total else 0.0,
        "sena_pct": round(100 * tally["joint"] / total, 2) if total else 0.0,
    }


def load_benchmark(directory: Path, selected: set[str] | None = None) -> dict[tuple[str, str], dict]:
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    rows = {}
    for language, meta in manifest["languages"].items():
        if selected is not None and language not in selected:
            continue
        path = directory / meta["file"]
        for row in load_jsonl(path):
            rows[(language, row["id"])] = row
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmark", type=Path, default=DEFAULT_BENCHMARK)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--pred-a", type=Path, required=True)
    parser.add_argument("--pred-b", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--signals", type=Path, default=None)
    parser.add_argument("--languages", default="", help="comma-separated language-code subset")
    parser.add_argument("--encoder", default=DEFAULT_ENCODER)
    parser.add_argument("--encoder-lang", default="en")
    parser.add_argument("--delta", type=float, default=0.10)
    parser.add_argument("--epsilon", type=float, default=1e-6)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = parser.parse_args()

    selected = {item for item in args.languages.split(",") if item} or None
    benchmark = load_benchmark(args.benchmark, selected)
    mapping = load_jsonl(args.manifest)
    prediction_rows = {
        "a": load_jsonl(args.pred_a),
        "b": load_jsonl(args.pred_b),
    }
    pair_map: dict[tuple[str, str], dict] = defaultdict(dict)
    for row in mapping:
        side = row.get("side")
        if side not in {"a", "b"}:
            raise SystemExit(f"invalid manifest side: {side!r}")
        key = (row["language"], row["sample_id"])
        if side in pair_map[key]:
            raise SystemExit(f"duplicate manifest mapping: {key} side {side}")
        pair_map[key][side] = row

    expected_inputs = {"a": [], "b": []}
    for (language, sample_id), sides in pair_map.items():
        source = benchmark.get((language, sample_id))
        if source is None:
            raise SystemExit(f"manifest references unknown sample: {(language, sample_id)}")
        for side in ("a", "b"):
            if side not in sides:
                raise SystemExit(f"missing manifest side: {(language, sample_id)} {side}")
            expected_inputs[side].append({
                "id": sides[side]["input_id"],
                "language": language,
                "text": source[side],
            })
    for side in ("a", "b"):
        errors = validate(expected_inputs[side], prediction_rows[side])
        if errors:
            raise SystemExit("invalid side-{} predictions:\n{}".format(
                side, "\n".join(f"- {error}" for error in errors)
            ))
    predictions = {
        side: {row["id"]: row for row in prediction_rows[side]}
        for side in ("a", "b")
    }

    records = []
    for key in sorted(benchmark):
        source = benchmark[key]
        sides = pair_map.get(key, {})
        if set(sides) != {"a", "b"}:
            raise SystemExit(f"missing private mapping for {key}")
        outputs, valid = {}, True
        for side in ("a", "b"):
            prediction = predictions[side].get(sides[side]["input_id"])
            if (prediction is None or prediction.get("status") != "ok"
                    or not isinstance(prediction.get("canonical_text"), str)):
                valid = False
                outputs[side] = source[side]
            else:
                outputs[side] = prediction["canonical_text"]
        records.append({
            "id": source["id"],
            "language": key[0],
            "category": source["category"],
            "phenomenon": source["phenomenon"],
            "a": source["a"],
            "b": source["b"],
            "canonical_a": outputs["a"],
            "canonical_b": outputs["b"],
            "valid": valid,
        })

    scorer = BERTScorer(
        model_type=args.encoder,
        lang=args.encoder_lang,
        device=args.device,
        batch_size=args.batch_size,
        idf=False,
        rescale_with_baseline=False,
    )
    t_values = score_f1(scorer, [r["a"] for r in records], [r["b"] for r in records])
    f_a_values = score_f1(
        scorer, [r["canonical_a"] for r in records], [r["a"] for r in records]
    )
    f_b_values = score_f1(
        scorer, [r["canonical_b"] for r in records], [r["b"] for r in records]
    )

    overall = new_tally()
    by_language, by_category, by_phenomenon = {}, {}, {}
    signals = []
    for record, t_value, f_a, f_b in zip(records, t_values, f_a_values, f_b_values):
        fidelity = min(f_a, f_b)
        exact = record["valid"] and record["canonical_a"] == record["canonical_b"]
        semantic = record["valid"] and fidelity + args.delta + args.epsilon >= t_value
        joint = exact and semantic
        add(overall, exact, semantic, joint)
        keys = (
            (record["language"], by_language),
            (record["category"], by_category),
            (f"{record['category']}/{record['phenomenon']}", by_phenomenon),
        )
        for key, table in keys:
            table.setdefault(key, new_tally())
            add(table[key], exact, semantic, joint)
        signals.append({
            "id": record["id"],
            "language": record["language"],
            "category": record["category"],
            "phenomenon": record["phenomenon"],
            "t": round(t_value, 6),
            "f_a": round(f_a, 6),
            "f_b": round(f_b, 6),
            "f": round(fidelity, 6),
            "exact": exact,
            "semantic": semantic,
            "score": int(joint),
        })

    report = {
        "metric": "Semantic-preserving Exact-match Normalization Accuracy (SENA)",
        "configuration": {
            "encoder": args.encoder,
            "encoder_lang": args.encoder_lang,
            "idf": False,
            "rescale_with_baseline": False,
            "delta": args.delta,
            "epsilon": args.epsilon,
            "exact_match": "raw string equality",
        },
        "overall": finish(overall),
        "by_language": {key: finish(value) for key, value in sorted(by_language.items())},
        "by_category": {key: finish(value) for key, value in sorted(by_category.items())},
        "by_phenomenon": {key: finish(value) for key, value in sorted(by_phenomenon.items())},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.signals:
        args.signals.parent.mkdir(parents=True, exist_ok=True)
        with args.signals.open("w", encoding="utf-8") as handle:
            for row in signals:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"SENA: {report['overall']['sena_pct']:.2f}")
    print(args.output)


if __name__ == "__main__":
    main()

