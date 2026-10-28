#!/usr/bin/env python3
"""Canonicalize an ETC JSONL batch with a released small model."""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from inference import generate, load_canonicalizer


INPUT_FIELDS = {"id", "language", "text"}


def load_input(path: Path) -> list[dict]:
    rows = []
    seen = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if not isinstance(row, dict) or set(row) != INPUT_FIELDS:
            raise SystemExit(f"{path}:{line_number}: expected fields {sorted(INPUT_FIELDS)}")
        if not all(isinstance(row[field], str) and row[field] for field in INPUT_FIELDS):
            raise SystemExit(f"{path}:{line_number}: all fields must be non-empty strings")
        if row["id"] in seen:
            raise SystemExit(f"{path}:{line_number}: duplicate id {row['id']!r}")
        seen.add(row["id"])
        rows.append(row)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="local model directory or hub identifier")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--max-new-tokens", type=int, default=256)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--dtype", choices=["auto", "float32", "float16", "bfloat16"], default="auto")
    args = parser.parse_args()

    rows = load_input(args.input)
    tokenizer, model, device = load_canonicalizer(args.model, args.device, args.dtype)
    started = time.time()
    predictions = generate(
        tokenizer,
        model,
        [row["text"] for row in rows],
        device=device,
        batch_size=args.batch_size,
        max_new_tokens=args.max_new_tokens,
        on_progress=lambda done, total: print(f"{done}/{total}", flush=True),
    )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        for row, prediction in zip(rows, predictions):
            handle.write(json.dumps({
                "id": row["id"],
                "canonical_text": prediction,
                "status": "ok",
                "error": None,
            }, ensure_ascii=False) + "\n")

    changed = sum(row["text"] != prediction for row, prediction in zip(rows, predictions))
    stats = {
        "model": args.model,
        "records": len(rows),
        "changed": changed,
        "elapsed_seconds": round(time.time() - started, 2),
        "batch_size": args.batch_size,
        "max_new_tokens": args.max_new_tokens,
        "device": device,
        "dtype": args.dtype,
    }
    args.out.with_suffix(".runstats.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(args.out)


if __name__ == "__main__":
    main()

