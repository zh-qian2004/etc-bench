#!/usr/bin/env python3
"""Validate ETC batch JSONL correspondence and output schema."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

INPUT_FIELDS = {"id", "language", "text"}
OUTPUT_FIELDS = {"id", "canonical_text", "status", "error"}


def load_jsonl(path: Path) -> tuple[list[dict], list[str]]:
    rows, errors = [], []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"{path}:{line_no}: invalid JSON: {exc.msg}")
                continue
            if not isinstance(row, dict):
                errors.append(f"{path}:{line_no}: record must be an object")
                continue
            rows.append(row)
    return rows, errors


def validate(input_path: Path, output_path: Path, strict_input: bool) -> list[str]:
    inputs, errors = load_jsonl(input_path)
    outputs, output_errors = load_jsonl(output_path)
    errors.extend(output_errors)
    seen: set[str] = set()
    for index, row in enumerate(inputs, 1):
        if strict_input and set(row) != INPUT_FIELDS:
            errors.append(f"input record {index}: fields must be {sorted(INPUT_FIELDS)}")
        rid = row.get("id")
        if not isinstance(rid, str) or not rid:
            errors.append(f"input record {index}: id must be a non-empty string")
        elif rid in seen:
            errors.append(f"input record {index}: duplicate id {rid!r}")
        else:
            seen.add(rid)
        if not isinstance(row.get("language"), str) or not row.get("language"):
            errors.append(f"input record {index}: language must be a non-empty string")
        if not isinstance(row.get("text"), str):
            errors.append(f"input record {index}: text must be a string")
    if len(outputs) != len(inputs):
        errors.append(f"record count differs: input={len(inputs)} output={len(outputs)}")
    for index, (source, result) in enumerate(zip(inputs, outputs), 1):
        if set(result) != OUTPUT_FIELDS:
            errors.append(f"output record {index}: fields must be {sorted(OUTPUT_FIELDS)}")
        if result.get("id") != source.get("id"):
            errors.append(f"output record {index}: id/order mismatch")
        status = result.get("status")
        if status == "ok":
            if not isinstance(result.get("canonical_text"), str):
                errors.append(f"output record {index}: ok requires string canonical_text")
            if result.get("error") is not None:
                errors.append(f"output record {index}: ok requires null error")
        elif status == "error":
            if result.get("canonical_text") is not None:
                errors.append(f"output record {index}: error requires null canonical_text")
            if not isinstance(result.get("error"), str) or not result.get("error"):
                errors.append(f"output record {index}: error requires non-empty error")
        else:
            errors.append(f"output record {index}: status must be ok or error")
    return errors


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--allow-extra-input-fields", action="store_true")
    args = ap.parse_args()
    errors = validate(args.input, args.output, not args.allow_extra_input_fields)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print(f"batch valid: {args.output}")


if __name__ == "__main__":
    main()

