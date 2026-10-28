#!/usr/bin/env python3
"""Validate the shared ETC input and prediction JSONL contract."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


INPUT_FIELDS = {"id", "language", "text"}
OUTPUT_FIELDS = {"id", "canonical_text", "status", "error"}


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"{path}:{line_number}: invalid JSON: {error.msg}") from error
        if not isinstance(row, dict):
            raise ValueError(f"{path}:{line_number}: record must be an object")
        rows.append(row)
    return rows


def validate(input_rows: list[dict], prediction_rows: list[dict]) -> list[str]:
    errors = []
    if len(input_rows) != len(prediction_rows):
        errors.append(
            f"record count differs: input={len(input_rows)} predictions={len(prediction_rows)}"
        )
    input_ids, output_ids = set(), set()
    for index, row in enumerate(input_rows, 1):
        if set(row) != INPUT_FIELDS:
            errors.append(f"input record {index}: fields must be {sorted(INPUT_FIELDS)}")
        row_id = row.get("id")
        if not isinstance(row_id, str) or not row_id:
            errors.append(f"input record {index}: invalid id")
        elif row_id in input_ids:
            errors.append(f"input record {index}: duplicate id {row_id!r}")
        input_ids.add(row_id)
    for index, row in enumerate(prediction_rows, 1):
        if set(row) != OUTPUT_FIELDS:
            errors.append(f"prediction record {index}: fields must be {sorted(OUTPUT_FIELDS)}")
        row_id = row.get("id")
        if not isinstance(row_id, str) or not row_id:
            errors.append(f"prediction record {index}: invalid id")
        elif row_id in output_ids:
            errors.append(f"prediction record {index}: duplicate id {row_id!r}")
        output_ids.add(row_id)
        if row.get("status") == "ok":
            if not isinstance(row.get("canonical_text"), str):
                errors.append(f"prediction record {index}: ok requires string canonical_text")
            if row.get("error") is not None:
                errors.append(f"prediction record {index}: ok requires null error")
        elif row.get("status") == "error":
            if row.get("canonical_text") is not None:
                errors.append(f"prediction record {index}: error requires null canonical_text")
            if not isinstance(row.get("error"), str) or not row.get("error"):
                errors.append(f"prediction record {index}: error requires a reason")
        else:
            errors.append(f"prediction record {index}: status must be ok or error")
    missing = input_ids - output_ids
    extra = output_ids - input_ids
    if missing:
        errors.append(f"missing prediction ids: {len(missing)}")
    if extra:
        errors.append(f"unexpected prediction ids: {len(extra)}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("predictions", type=Path)
    args = parser.parse_args()
    errors = validate(load_jsonl(args.input), load_jsonl(args.predictions))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print(f"valid: {args.predictions}")


if __name__ == "__main__":
    main()

