# Shared ETC-Bench evaluation

Every ETC system is evaluated through the same three steps.

1. `prepare_inputs.py` independently shuffles pair sides and writes a private assembly manifest.
2. The system canonicalizes the two input files independently and emits `{id, canonical_text, status, error}` records.
3. `evaluate_sena.py` restores the pair mapping and reports SENA overall and by language, category, and phenomenon.

```bash
python evaluation/prepare_inputs.py --output-dir work/input

# Run a tool independently on work/input/input-a.jsonl and input-b.jsonl.

python evaluation/validate_predictions.py \
  work/input/input-a.jsonl work/output-a.jsonl

python evaluation/evaluate_sena.py \
  --manifest work/input/_manifest.jsonl \
  --pred-a work/output-a.jsonl \
  --pred-b work/output-b.jsonl \
  --output work/sena.json
```

The default configuration matches the paper: `xlm-roberta-large`, no IDF weighting or baseline rescaling, exact string equality, and `delta=0.10`.

