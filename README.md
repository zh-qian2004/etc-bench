# ETC-Bench

ETC-Bench is a multilingual benchmark for **evaluation-side transcript canonicalization (ETC)**. ETC maps multiple written surface forms of the same speech to one canonical form before a system transcript and its reference are compared. The benchmark tests whether a canonicalizer makes speech-equivalent transcript variants identical while limiting changes to their semantic content.

## Repository contents

```text
etc-bench/
├── benchmark/                  # ETC-Bench release data and manifest
├── evaluation/                 # Shared input preparation and SENA evaluator
├── tools/
│   ├── tacs/                   # Taxonomy-Guided Agent Canonicalization Skill
│   └── model-canonicalizer/    # Inference code for the released small models
├── CITATION.cff
├── README.md
└── requirements.txt
```

## Benchmark

The release contains **1,098 minimal pairs**, **181 canonicalization phenomena**, and **12 languages**:

| Code | Language | Pairs |
|---|---|---:|
| `ar` | Arabic | 86 |
| `bn` | Bengali | 98 |
| `de` | German | 93 |
| `en` | English | 88 |
| `fa` | Persian | 80 |
| `fr` | French | 89 |
| `hi` | Hindi | 100 |
| `id` | Indonesian | 98 |
| `ja` | Japanese | 76 |
| `ru` | Russian | 100 |
| `vi` | Vietnamese | 98 |
| `zh` | Mandarin Chinese | 92 |

The taxonomy has five categories: `numeric_expressions`, `symbols_markers`, `abbreviations`, `orthographic_variants`, and `homophonic_substitutions`. Numeric expressions and symbols and markers use language-agnostic phenomenon definitions. The other three categories contain language-specific phenomena.

Each language file in `benchmark/` is UTF-8 JSONL. Every record has exactly these fields:

```json
{
  "id": "2291",
  "language": "en",
  "category": "symbols_markers",
  "phenomenon": "biological",
  "phenomenon_description": "A biological classification written as a code that is read aloud as a name.",
  "a": "They were treated for HPV.",
  "b": "They were treated for H P V."
}
```

- `id`: sample identifier, unique in the release;
- `language`: ISO 639-1 language code;
- `category`: one of the five taxonomy categories;
- `phenomenon`: canonicalization phenomenon identifier;
- `phenomenon_description`: natural-language definition of the phenomenon;
- `a`, `b`: independently canonicalizable members of a speech-equivalent minimal pair.

`benchmark/manifest.json` records the released files, row counts, version, and SHA-256 checksums.

## Installation

Python 3.11 is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The evaluator downloads `xlm-roberta-large` through Hugging Face on first use. GPU acceleration is recommended for full-benchmark SENA evaluation but is not required by the file-preparation and validation scripts.

## Shared batch interface

Every canonicalizer consumes UTF-8 JSONL records of the form:

```json
{"id":"opaque-id","language":"en","text":"The recipe calls for two eggs."}
```

and emits one record per input, preserving order and IDs:

```json
{"id":"opaque-id","canonical_text":"The recipe calls for 2 eggs.","status":"ok","error":null}
```

An unsuccessful record uses `"status":"error"`, a null `canonical_text`, and a non-empty `error` string.

## Evaluation with SENA

Prepare independently shuffled inputs for the two members of every pair:

```bash
python evaluation/prepare_inputs.py --output-dir work/input
```

Apply the same canonicalizer independently to `work/input/input-a.jsonl` and `work/input/input-b.jsonl`. Do not expose `work/input/_manifest.jsonl` to the canonicalizer. Validate each output before scoring:

```bash
python evaluation/validate_predictions.py \
  work/input/input-a.jsonl work/output-a.jsonl

python evaluation/validate_predictions.py \
  work/input/input-b.jsonl work/output-b.jsonl
```

Then compute **Semantic-Preserving Exact-Match Normalization Accuracy (SENA)**:

```bash
python evaluation/evaluate_sena.py \
  --manifest work/input/_manifest.jsonl \
  --pred-a work/output-a.jsonl \
  --pred-b work/output-b.jsonl \
  --output work/sena.json
```

A pair receives credit only when the two canonical outputs are exactly equal and their pair-relative BERTScore satisfies the semantic-preservation condition. The released evaluator reports SENA overall and by language, category, and phenomenon. Its paper configuration uses `xlm-roberta-large`, no IDF weighting or baseline rescaling, raw string equality, and the pre-fixed tolerance `delta=0.10`. See [`evaluation/README.md`](evaluation/README.md) for the compact evaluation protocol.

## TACS

[`tools/tacs/`](tools/tacs/) contains the **Taxonomy-Guided Agent Canonicalization Skill (TACS)**. It gives an agent:

- the released phenomenon taxonomy;
- language-indexed canonicalization contracts;
- a five-stage recognition and local-edit method;
- batch input, output, trace, and validation contracts.

TACS is a methodology skill: the agent remains the canonicalization solver. Its scripts validate files and check benchmark isolation; they do not implement a rule-based canonicalizer. See [`tools/tacs/README.md`](tools/tacs/README.md) for the invocation prompt and full structure.

## Released model canonicalizers

We also release two supervised ETC canonicalizers derived from Qwen3.5:

| Model | Base model | Parameters | Epochs | ETC-Bench SENA | Weights |
|---|---|---:|---:|---:|---|
| ETC-Qwen3.5-4B | Qwen3.5-4B | 4B | 3 | 59.2 | [`zhiheng-qian/etc-qwen3.5-4b`](https://huggingface.co/zhiheng-qian/etc-qwen3.5-4b) |
| ETC-Qwen3.5-0.8B | Qwen3.5-0.8B | 0.8B | 3 | 43.6 | [`zhiheng-qian/etc-qwen3.5-0.8b`](https://huggingface.co/zhiheng-qian/etc-qwen3.5-0.8b) |

Both models were fine-tuned with the same system instruction on a mixture drawn from 32,718 teacher-canonicalized FLEURS training records, 8,735 teacher-canonicalized FLEURS test records, and 8,547 records from the unused ETC-Bench generation pool. Exact released pair IDs, pairs, and transcript strings were excluded when constructing the generation-pool component. No-op training records were downsampled with a keep ratio of 0.3. Common settings were three epochs, seed 42, maximum sequence length 512, answer-only supervised loss, and greedy inference with thinking disabled.

The reported SENA values use the shared evaluator above with `delta=0.10`. The exact inference instruction is preserved in [`tools/model-canonicalizer/prompt.txt`](tools/model-canonicalizer/prompt.txt), including its original terminology. Inference code and model identifiers are provided in [`tools/model-canonicalizer/`](tools/model-canonicalizer/). Training code, optimizer states, and intermediate checkpoints are not included in this release.

Example inference:

```bash
python tools/model-canonicalizer/predict.py \
  --model zhiheng-qian/etc-qwen3.5-4b \
  --input work/input/input-a.jsonl \
  --out work/output-a.jsonl \
  --device auto \
  --batch-size 16
```

The same command can be run for `input-b.jsonl`. CUDA, Ascend NPU, and CPU execution are supported; `torch_npu` and CANN are required only for Ascend NPU inference.

## Citation

Citation metadata for this repository is provided in [`CITATION.cff`](CITATION.cff). Until a final proceedings record is available, the resource can be cited as:

```bibtex
@misc{qian2026etcbench,
  title        = {ETC-Bench: A Multilingual Benchmark for Evaluation-Side Transcript Canonicalization},
  author       = {Zhiheng Qian and Junhao Du and Jing Peng and Hanqi Li and Kunyang Peng and Feng Xue and Shuai Wang and Kai Yu},
  year         = {2026},
  howpublished = {GitHub repository},
  url          = {https://github.com/zh-qian2004/etc-bench}
}
```
