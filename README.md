<h1 align="center">ETC-Bench</h1>

<p align="center"><strong>A multilingual benchmark for evaluation-side transcript canonicalization</strong></p>

<p align="center">
<a href="https://arxiv.org/abs/2610.36527"><strong>Paper ↗</strong></a> ·
<a href="#quick-start"><strong>Quick Start</strong></a> ·
<a href="#tacs"><strong>TACS</strong></a> ·
<a href="#model-canonicalizers"><strong>Models</strong></a>
</p>

<p align="center"><strong>English</strong> · <a href="README.zh-CN.md">简体中文</a></p>

<p align="center">
<a href="#why-etc">Why ETC?</a> · <a href="#whats-in-this-repository">Resources</a> ·
<a href="#etc-bench">Benchmark</a> · <a href="#sena">Metric</a> ·
<a href="#citation">Citation</a>
</p>

---

ETC-Bench evaluates **evaluation-side transcript canonicalization (ETC)**: independently mapping multiple written surface forms of the same speech to one canonical form before a system transcript and its reference are compared.

<p align="center"><strong>1,098</strong> minimal pairs &nbsp;·&nbsp; <strong>181</strong> phenomena &nbsp;·&nbsp; <strong>12</strong> languages &nbsp;·&nbsp; <strong>5</strong> categories</p>

## Why ETC?

Speech does not always determine a unique written transcript. Numeric expressions, abbreviations, spelling variants, symbols, and homophones can produce different valid surface forms for the same utterance. Direct text comparison may therefore count a representational choice as a system error.

ETC applies the **same canonicalizer independently** to the system transcript and the reference:

| Transcript A | Transcript B | Shared canonical form |
|---|---|---|
| `The recipe calls for two eggs.` | `The recipe calls for 2 eggs.` | `The recipe calls for 2 eggs.` |

ETC does not prescribe whether the target should resemble conventional text normalization (TN) or inverse text normalization (ITN). Either direction can be used as long as the selected canonical form is deterministic and preserves the relevant semantic information.

## What's in this repository?

| Component | Purpose |
|---|---|
| [`benchmark/`](benchmark/) | ETC-Bench release: 1,098 speech-equivalent minimal pairs |
| [`evaluation/`](evaluation/) | Shared input preparation, validation, and SENA evaluation |
| [`tools/tacs/`](tools/tacs/) | Taxonomy-Guided Agent Canonicalization Skill |
| [`tools/model-canonicalizer/`](tools/model-canonicalizer/) | Inference code for the released 4B and 0.8B canonicalizers |
| [`CITATION.cff`](CITATION.cff) | Machine-readable citation metadata |

## ETC-Bench

Each benchmark item is a minimal pair in a shared sentence context. The two members differ only in a target span exhibiting one canonicalization phenomenon.

### Taxonomy

| Category | Scope | What varies |
|---|---|---|
| Numeric Expressions | Language-agnostic | Written formats and spoken realizations of numbers |
| Symbols & Markers | Language-agnostic | Non-word symbolic expressions and markers |
| Abbreviations | Language-specific | Abbreviated and expanded word forms |
| Orthographic Variants | Language-specific | Alternative written forms of the same word |
| Homophonic Substitutions | Language-specific | Written distinctions that speech does not resolve |

<details>
<summary><strong>Language coverage and pair counts</strong></summary>

| Code | Language | Pairs | Code | Language | Pairs |
|---|---|---:|---|---|---:|
| `ar` | Arabic | 86 | `hi` | Hindi | 100 |
| `bn` | Bengali | 98 | `id` | Indonesian | 98 |
| `de` | German | 93 | `ja` | Japanese | 76 |
| `en` | English | 88 | `ru` | Russian | 100 |
| `fa` | Persian | 80 | `vi` | Vietnamese | 98 |
| `fr` | French | 89 | `zh` | Mandarin Chinese | 92 |

</details>

<details>
<summary><strong>Record schema</strong></summary>

Every language file in `benchmark/` is UTF-8 JSONL. Each record contains:

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
- `a`, `b`: independently canonicalizable members of the minimal pair.

[`benchmark/manifest.json`](benchmark/manifest.json) records the released files, version, row counts, and SHA-256 checksums.

</details>

## Quick Start

Python 3.11 is recommended.

```bash
git clone https://github.com/zh-qian2004/etc-bench.git
cd etc-bench
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 1. Prepare independent pair sides

```bash
python evaluation/prepare_inputs.py --output-dir work/input
```

This writes independently shuffled `input-a.jsonl` and `input-b.jsonl` files plus a private assembly manifest. Do not expose `_manifest.jsonl` to the canonicalizer.

Each input record has the shared batch interface:

```json
{"id":"opaque-id","language":"en","text":"The recipe calls for two eggs."}
```

### 2. Canonicalize both sides independently

Run any ETC system separately on the two input files. For example, with the released 4B model:

```bash
python tools/model-canonicalizer/predict.py \
  --model zhiheng-qian/etc-qwen3.5-4b \
  --input work/input/input-a.jsonl \
  --out work/output-a.jsonl \
  --device auto --batch-size 16

python tools/model-canonicalizer/predict.py \
  --model zhiheng-qian/etc-qwen3.5-4b \
  --input work/input/input-b.jsonl \
  --out work/output-b.jsonl \
  --device auto --batch-size 16
```

Every output record must preserve the input ID:

```json
{"id":"opaque-id","canonical_text":"The recipe calls for 2 eggs.","status":"ok","error":null}
```

### 3. Validate and evaluate

```bash
python evaluation/validate_predictions.py \
  work/input/input-a.jsonl work/output-a.jsonl

python evaluation/validate_predictions.py \
  work/input/input-b.jsonl work/output-b.jsonl

python evaluation/evaluate_sena.py \
  --manifest work/input/_manifest.jsonl \
  --pred-a work/output-a.jsonl \
  --pred-b work/output-b.jsonl \
  --output work/sena.json
```

The evaluator downloads `xlm-roberta-large` on first use. GPU acceleration is recommended for full-benchmark evaluation. See [`evaluation/README.md`](evaluation/README.md) for the compact protocol and language-subset options.

## SENA

**Semantic-Preserving Exact-Match Normalization Accuracy (SENA)** awards a pair credit only when:

1. its independently canonicalized members are exactly equal; and
2. the pair-relative BERTScore condition permits the observed decrease in similarity.

The released evaluator reports SENA overall and by language, category, and phenomenon. The paper configuration uses `xlm-roberta-large`, no IDF weighting or baseline rescaling, raw string equality, and the pre-fixed tolerance `delta=0.10`.

## TACS

[`tools/tacs/`](tools/tacs/) contains the **Taxonomy-Guided Agent Canonicalization Skill (TACS)**. It provides an agent with:

- a closed inventory of language-agnostic and language-specific phenomena;
- language-indexed canonicalization contracts;
- a five-stage recognition and local-edit method;
- batch input, output, trace, and validation contracts.

TACS is a methodology skill: the agent remains the solver. Its scripts validate files and check benchmark isolation; they do not implement a rule-based canonicalizer.

```text
Use $taxonomy-guided-agent-canonicalization-skill.

Canonicalize the UTF-8 JSONL records in:
{{input_path}}

Write the validated JSONL results to:
{{output_path}}
```

See [`tools/tacs/README.md`](tools/tacs/README.md) for the complete invocation prompt and skill structure.

## Model canonicalizers

We release two supervised ETC canonicalizers derived from Qwen3.5:

| Model | Base model | Epochs | ETC-Bench SENA | Weights |
|---|---|---:|---:|---|
| ETC-Qwen3.5-4B | Qwen3.5-4B | 3 | 59.2 | [Hugging Face](https://huggingface.co/zhiheng-qian/etc-qwen3.5-4b) |
| ETC-Qwen3.5-0.8B | Qwen3.5-0.8B | 3 | 43.6 | [Hugging Face](https://huggingface.co/zhiheng-qian/etc-qwen3.5-0.8b) |

Both use greedy decoding with thinking disabled. The exact inference instruction is preserved in [`tools/model-canonicalizer/prompt.txt`](tools/model-canonicalizer/prompt.txt), including its original terminology. Training code, optimizer states, and intermediate checkpoints are not included.

<details>
<summary><strong>Training data and common settings</strong></summary>

The training mixture was drawn from:

- 32,718 teacher-canonicalized FLEURS training records;
- 8,735 teacher-canonicalized FLEURS test records;
- 8,547 records from the unused ETC-Bench generation pool.

Exact released pair IDs, pairs, and transcript strings were excluded when constructing the generation-pool component. No-op records were downsampled with a keep ratio of `0.3`. Common settings were three epochs, seed `42`, maximum sequence length `512`, and answer-only supervised loss.

</details>

CUDA, Ascend NPU, and CPU inference are supported. `torch_npu` and CANN are required only for Ascend NPU execution. Model identifiers and additional inference notes are in [`tools/model-canonicalizer/`](tools/model-canonicalizer/).

## Repository layout

```text
etc-bench/
├── benchmark/                  # Release JSONL files and manifest
├── evaluation/                 # Shared SENA evaluation
├── tools/
│   ├── tacs/                   # Agent skill, taxonomy, and contracts
│   └── model-canonicalizer/    # Small-model inference
├── CITATION.cff
├── README.md
└── README.zh-CN.md
```

## Citation

If ETC-Bench, SENA, TACS, or the released canonicalizers are useful in your research, please cite [our paper](https://arxiv.org/abs/2610.36527):

```bibtex
@misc{qian2026etcbench,
  title={ETC-Bench: A Multilingual Benchmark for Evaluation-Side Transcript Canonicalization},
  author={Zhiheng Qian and Junhao Du and Jing Peng and Hanqi Li and
    Kunyang Peng and Feng Xue and Kai Yu},
  year={2026},
  eprint={2610.36527},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2610.36527}
}
```

Machine-readable metadata is available in [`CITATION.cff`](CITATION.cff).
