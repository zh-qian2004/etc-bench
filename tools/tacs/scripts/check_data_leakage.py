#!/usr/bin/env python3
"""Fail if skill Markdown reproduces a benchmark sample sentence.

This is a guardrail, not a proof of zero contamination. It deliberately reads
test data only during repository-side validation; test content is never copied
into the skill.
"""
from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    skill = Path(__file__).resolve().parents[1]
    root = skill.parents[1]
    bench = root / "benchmark"
    corpus = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in skill.rglob("*.md"))
    collisions = []
    candidates = list(bench.glob("*.jsonl"))
    for path in candidates:
        for number, line in enumerate(path.open(encoding="utf-8"), 1):
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            for field in ("a", "b"):
                value = row.get(field)
                if isinstance(value, str) and len(value.strip()) >= 12 and value in corpus:
                    collisions.append(f"{path}:{number}:{field}")
    if collisions:
        print("benchmark sentence collision(s):")
        print("\n".join(collisions))
        raise SystemExit(1)
    print("no full benchmark-sentence collisions")


if __name__ == "__main__":
    main()

