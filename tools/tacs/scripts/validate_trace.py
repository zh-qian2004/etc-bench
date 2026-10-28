#!/usr/bin/env python3
"""Validate batch trace sidecar structure and edit reconstruction."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED_CATEGORIES = {
    "numeric_expressions", "symbols_markers", "abbreviations",
    "orthographic_variants", "homophonic_substitutions",
}


def load(path: Path) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{path}:{line_no}: invalid JSON: {exc.msg}")
            if not isinstance(row, dict):
                raise SystemExit(f"{path}:{line_no}: record must be an object")
            rows.append(row)
    return rows


def occurrences(text: str, quote: str) -> list[int]:
    found, start = [], 0
    while quote:
        pos = text.find(quote, start)
        if pos < 0:
            break
        found.append(pos)
        start = pos + len(quote)
    return found


def validate_record(text: str, canonical: str, trace: dict, index: int) -> list[str]:
    errors, resolved = [], []
    edits = trace.get("edits")
    if set(trace) != {"id", "edits"} or not isinstance(edits, list):
        return [f"trace record {index}: fields must be id and edits"]
    for edit_index, edit in enumerate(edits, 1):
        prefix = f"trace record {index} edit {edit_index}"
        quote, occurrence = edit.get("quote"), edit.get("occurrence", 1)
        if not isinstance(quote, str) or not quote:
            errors.append(f"{prefix}: quote must be non-empty")
            continue
        if not isinstance(occurrence, int) or occurrence < 1:
            errors.append(f"{prefix}: occurrence must be positive")
            continue
        hits = occurrences(text, quote)
        if occurrence > len(hits):
            errors.append(f"{prefix}: occurrence does not exist")
            continue
        required = {"quote", "occurrence", "category", "phenomenon", "semantic_value", "replacement", "confidence"}
        if set(edit) != required:
            errors.append(f"{prefix}: incorrect fields")
        if edit.get("category") not in ALLOWED_CATEGORIES:
            errors.append(f"{prefix}: invalid category")
        if not isinstance(edit.get("phenomenon"), str) or not edit.get("phenomenon"):
            errors.append(f"{prefix}: phenomenon must be non-empty")
        if edit.get("confidence") != "high":
            errors.append(f"{prefix}: confidence must be high")
        replacement = edit.get("replacement")
        if not isinstance(replacement, str):
            errors.append(f"{prefix}: replacement must be a string")
            continue
        start = hits[occurrence - 1]
        resolved.append((start, start + len(quote), replacement, prefix))
    ordered = sorted(resolved)
    for left, right in zip(ordered, ordered[1:]):
        if left[1] > right[0]:
            errors.append(f"{left[3]} overlaps {right[3]}")
    rebuilt = text
    for start, end, replacement, _ in reversed(ordered):
        rebuilt = rebuilt[:start] + replacement + rebuilt[end:]
    if rebuilt != canonical:
        errors.append(f"trace record {index}: edits do not reconstruct canonical_text")
    return errors


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("trace", type=Path)
    args = ap.parse_args()
    inputs, outputs, traces = load(args.input), load(args.output), load(args.trace)
    successful = [(source, result) for source, result in zip(inputs, outputs)
                  if result.get("status") == "ok"]
    errors = []
    if len(inputs) != len(outputs):
        errors.append("input/output record counts differ")
    if len(traces) != len(successful):
        errors.append(f"trace count differs: successful={len(successful)} trace={len(traces)}")
    for index, ((source, result), trace) in enumerate(zip(successful, traces), 1):
        if trace.get("id") != source.get("id") or result.get("id") != source.get("id"):
            errors.append(f"trace record {index}: id/order mismatch")
            continue
        errors.extend(validate_record(source.get("text", ""), result.get("canonical_text", ""), trace, index))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print(f"trace valid: {args.trace}")


if __name__ == "__main__":
    main()

