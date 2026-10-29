#!/usr/bin/env python3
"""Build the static ETC-Bench demo payload from benchmark and experiment artifacts."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


LANGUAGE_TO_RESULT_ID = {
    "ar": "ar-SA",
    "bn": "bn-BD",
    "de": "de-DE",
    "en": "en-US",
    "fa": "fa-IR",
    "fr": "fr-FR",
    "hi": "hi-IN",
    "id": "id-ID",
    "ja": "ja-JP",
    "ru": "ru-RU",
    "vi": "vi-VN",
    "zh": "zh-CN",
}

LANGUAGE_NAMES = {
    "ar": "Arabic",
    "bn": "Bengali",
    "de": "German",
    "en": "English",
    "fa": "Persian",
    "fr": "French",
    "hi": "Hindi",
    "id": "Indonesian",
    "ja": "Japanese",
    "ru": "Russian",
    "vi": "Vietnamese",
    "zh": "Mandarin Chinese",
}

CATEGORIES = [
    "numeric_expressions",
    "symbols_markers",
    "abbreviations",
    "orthographic_variants",
    "homophonic_substitutions",
]

CATEGORY_NAMES = {
    "numeric_expressions": "Numeric Expressions",
    "symbols_markers": "Symbols & Markers",
    "abbreviations": "Abbreviations",
    "orthographic_variants": "Orthographic Variants",
    "homophonic_substitutions": "Homophonic Substitutions",
}

TACS_REPORTED = {
    "tacs-gpt": {
        "label": "TACS–GPT",
        "model": "GPT-5.6-Terra",
        "score": 43.3,
        "languages": [51.9, 26.5, 42.7, 44.7, 62.1, 39.7, 40.0, 44.2, 38.6, 40.3, 46.6, 41.7],
        "categories": [44.1, 29.1, 53.4, 55.7, 20.0],
    },
    "tacs-deepseek": {
        "label": "TACS–DeepSeek",
        "model": "DeepSeek-V4-Flash",
        "score": 43.8,
        "languages": [42.6, 23.1, 49.8, 53.0, 47.9, 48.3, 31.0, 41.8, 42.5, 48.3, 55.8, 40.9],
        "categories": [50.4, 27.1, 56.0, 58.5, 12.1],
    },
    "tacs-qwen": {
        "label": "TACS–Qwen",
        "model": "Qwen3.8-Flash",
        "score": 68.8,
        "languages": [69.0, 67.7, 61.3, 65.5, 72.9, 73.0, 61.3, 75.2, 64.5, 75.3, 78.2, 62.0],
        "categories": [74.4, 44.3, 85.9, 82.3, 49.0],
    },
}


def read_jsonl(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def records_by_id(path: Path) -> dict[str, dict]:
    return {str(row["id"]): row for row in read_jsonl(path)}


def load_eval_summary(path: Path, system_key: str) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))["systems"][system_key]
    languages = {
        language: round(data["locales"][result_id]["overall"]["maen"], 1)
        for language, result_id in LANGUAGE_TO_RESULT_ID.items()
    }
    category_totals: dict[str, dict[str, int]] = defaultdict(lambda: {"total": 0, "joint": 0})
    for locale in data["locales"].values():
        for category, stats in locale["categories"].items():
            category_totals[category]["total"] += stats["total"]
            category_totals[category]["joint"] += stats["joint"]
    categories = {
        category: round(100 * values["joint"] / values["total"], 1)
        for category, values in category_totals.items()
    }
    return {
        "score": round(data["combined"]["maen"], 1),
        "languages": languages,
        "categories": categories,
    }


def load_outputs(norm_root: Path, gate_root: Path) -> dict[str, dict]:
    outputs: dict[str, dict] = {}
    for language, result_id in LANGUAGE_TO_RESULT_ID.items():
        norms = records_by_id(norm_root / f"{result_id}.jsonl")
        gates = records_by_id(gate_root / f"{result_id}.jsonl")
        for item_id, norm in norms.items():
            gate = gates[item_id]
            exact = bool(norm["norm_a"] == norm["norm_b"])
            semantic = float(gate["f"]) + 0.1 >= float(gate["t"])
            outputs[item_id] = {
                "a": norm["norm_a"],
                "b": norm["norm_b"],
                "exact": exact,
                "semantic": semantic,
                "credited": exact and semantic,
                "t": round(float(gate["t"]), 4),
                "f": round(float(gate["f"]), 4),
            }
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project-root",
        type=Path,
        required=True,
        help="Root of the internal masr-norm project containing results/ and runs/.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="ETC-Bench release repository root.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().with_name("data.js"),
    )
    args = parser.parse_args()

    project = args.project_root.resolve()
    repo = args.repo_root.resolve()
    language_order = list(LANGUAGE_TO_RESULT_ID)

    system_sources = {
        "tacs-gpt": (
            project / "results/masr-norm-bench/norms/gpt-5.6-terra-full-skill",
            project / "results/masr-norm-bench/gate_signals/qwen3.8-flash-skill-eval/gpt-5.6-terra-full-skill",
        ),
        "tacs-deepseek": (
            project / "results/masr-norm-bench/norms/deepseek-v4-flash-full-skill",
            project / "results/masr-norm-bench/gate_signals/qwen3.8-flash-skill-eval/deepseek-v4-flash-full-skill",
        ),
        "tacs-qwen": (
            project / "results/masr-norm-bench/norms/qwen3.8-flash-full-skill",
            project / "results/masr-norm-bench/gate_signals/qwen3.8-flash-skill-eval/qwen3.8-flash-full-skill",
        ),
        "model-4b": (
            project / "runs/distill-student/rescore-in-benchmix-e3/qwen3.5-4b-benchmix-e3",
            project / "runs/distill-student/gate_signals/qwen3.5-4b-benchmix-e3",
        ),
        "model-0.8b": (
            project / "runs/distill-student/rescore-in-0.8b-benchmix/qwen3.5-0.8b-benchmix",
            project / "runs/distill-student/gate_signals/qwen3.5-0.8b-benchmix",
        ),
    }
    outputs = {key: load_outputs(*paths) for key, paths in system_sources.items()}

    systems: list[dict] = []
    for key, source in TACS_REPORTED.items():
        representative = outputs[key]
        representative_score = round(
            100 * sum(row["credited"] for row in representative.values()) / len(representative), 1
        )
        systems.append({
            "id": key,
            "label": source["label"],
            "model": source["model"],
            "kind": "TACS agent",
            "score": source["score"],
            "scoreNote": "Mean of three runs reported in the paper",
            "outputRunScore": representative_score,
            "languages": dict(zip(language_order, source["languages"])),
            "categories": dict(zip(CATEGORIES, source["categories"])),
        })

    student_specs = [
        (
            "model-4b",
            "ETC-Qwen3.5-4B",
            "Qwen3.5-4B",
            project / "runs/distill-student/eval/release_eval_xlmr_gate_d10_qwen3.5-4b-benchmix-e3.json",
            "qwen3.5-4b-benchmix-e3",
        ),
        (
            "model-0.8b",
            "ETC-Qwen3.5-0.8B",
            "Qwen3.5-0.8B",
            project / "runs/distill-student/eval/release_eval_xlmr_gate_d10_qwen3.5-0.8b-benchmix.json",
            "qwen3.5-0.8b-benchmix",
        ),
    ]
    for key, label, model, eval_path, eval_key in student_specs:
        summary = load_eval_summary(eval_path, eval_key)
        systems.append({
            "id": key,
            "label": label,
            "model": model,
            "kind": "Model canonicalizer",
            "score": summary["score"],
            "scoreNote": "Single deterministic full-release evaluation",
            "outputRunScore": summary["score"],
            "languages": summary["languages"],
            "categories": summary["categories"],
        })

    items: list[dict] = []
    phenomenon_keys: set[tuple[str, str]] = set()
    for language in language_order:
        for row in read_jsonl(repo / "benchmark" / f"{language}.jsonl"):
            item_id = str(row["id"])
            item_outputs = {key: system[item_id] for key, system in outputs.items()}
            phenomenon_keys.add((row["category"], row["phenomenon"]))
            items.append({
                "id": item_id,
                "language": language,
                "category": row["category"],
                "phenomenon": row["phenomenon"],
                "description": row["phenomenon_description"],
                "a": row["a"],
                "b": row["b"],
                "outputs": item_outputs,
            })

    payload = {
        "meta": {
            "name": "ETC-Bench",
            "version": "1.0.0",
            "items": len(items),
            "languages": len(language_order),
            "phenomena": len(phenomenon_keys),
            "categories": len(CATEGORIES),
            "delta": 0.1,
            "encoder": "xlm-roberta-large",
        },
        "languageOrder": language_order,
        "languageNames": LANGUAGE_NAMES,
        "categoryOrder": CATEGORIES,
        "categoryNames": CATEGORY_NAMES,
        "systems": systems,
        "items": items,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "// Generated by demo/build_data.py. Do not edit by hand.\n"
        + "window.ETC_DEMO_DATA = "
        + json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
        + ";\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {args.output} with {len(items)} items, "
        f"{len(phenomenon_keys)} distinct phenomena, and {len(systems)} systems"
    )


if __name__ == "__main__":
    main()
