# ETC-Bench interactive demo

This directory contains a static browser for ETC-Bench and released canonicalization results. It lets visitors:

- browse all 1,098 benchmark pairs by language, category, and phenomenon;
- compare outputs from TACS instantiated with GPT, DeepSeek, and Qwen;
- inspect outputs from the released ETC-Qwen3.5-4B and ETC-Qwen3.5-0.8B model canonicalizers;
- see the exact-match condition, semantic-preservation condition, and per-item SENA credit;
- compare reported language- and category-level scores.

The page performs no inference. All outputs and metric signals are precomputed and bundled in `data.js`.

## Run locally

From the repository root:

```bash
python3 -m http.server 8765
```

Open <http://127.0.0.1:8765/demo/>.

## Rebuild the bundled data

The data builder expects the internal experiment workspace because released benchmark files alone do not contain system outputs:

```bash
python3 demo/build_data.py \
  --project-root /path/to/masr-norm \
  --repo-root /path/to/etc-bench
```

TACS headline scores are the three-run means reported in the paper. Pair-level TACS outputs come from one representative run and are identified as such in the interface. The two model canonicalizers use their deterministic full-release evaluations.
