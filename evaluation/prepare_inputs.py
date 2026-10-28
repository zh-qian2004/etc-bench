#!/usr/bin/env python3
"""Prepare independently shuffled ETC-Bench side-A and side-B inputs."""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
DEFAULT_BENCHMARK = REPOSITORY / "benchmark"
ID_SALT = "etc-bench-v1"


def opaque_id(language: str, sample_id: str, side: str) -> str:
    payload = f"{ID_SALT}|{language}|{sample_id}|{side}".encode("utf-8")
    return "e" + hashlib.sha256(payload).hexdigest()[:16]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmark", type=Path, default=DEFAULT_BENCHMARK)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, default=None)
    parser.add_argument("--languages", default="", help="comma-separated language-code subset")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    release_manifest = json.loads(
        (args.benchmark / "manifest.json").read_text(encoding="utf-8")
    )
    available = list(release_manifest["languages"])
    languages = [item for item in args.languages.split(",") if item] or available
    unknown = sorted(set(languages) - set(available))
    if unknown:
        raise SystemExit(f"unknown language code(s): {', '.join(unknown)}")

    records = {"a": [], "b": []}
    mapping = []
    for language in sorted(languages):
        path = args.benchmark / release_manifest["languages"][language]["file"]
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
                if line.strip()]
        for row in rows:
            for side in ("a", "b"):
                input_id = opaque_id(language, row["id"], side)
                records[side].append({
                    "id": input_id,
                    "language": language,
                    "text": row[side],
                })
                mapping.append({
                    "input_id": input_id,
                    "sample_id": row["id"],
                    "language": language,
                    "category": row["category"],
                    "phenomenon": row["phenomenon"],
                    "side": side,
                })

    random.Random(args.seed).shuffle(records["a"])
    random.Random(args.seed + 1).shuffle(records["b"])
    write_jsonl(args.output_dir / "input-a.jsonl", records["a"])
    write_jsonl(args.output_dir / "input-b.jsonl", records["b"])
    manifest_path = args.manifest or args.output_dir / "_manifest.jsonl"
    write_jsonl(manifest_path, mapping)
    print(f"side a: {len(records['a'])}")
    print(f"side b: {len(records['b'])}")
    print(f"private manifest: {manifest_path}")


if __name__ == "__main__":
    main()

