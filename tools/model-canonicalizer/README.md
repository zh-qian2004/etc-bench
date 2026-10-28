# Small-model ETC canonicalizer

This directory contains inference-only code for two fine-tuned ETC canonicalizers. Training code, optimizer state, and intermediate checkpoints are not part of the public release.

| Model | Parameters | ETC-Bench SENA | Weights |
|---|---:|---:|---|
| `etc-qwen3.5-4b` | 4B | 59.2 | [`zhiheng-qian/etc-qwen3.5-4b`](https://huggingface.co/zhiheng-qian/etc-qwen3.5-4b) |
| `etc-qwen3.5-0.8b` | 0.8B | 43.6 | [`zhiheng-qian/etc-qwen3.5-0.8b`](https://huggingface.co/zhiheng-qian/etc-qwen3.5-0.8b) |

The scores use the shared evaluator in `../../evaluation/` with `delta=0.10`. Published weight identifiers are recorded in `models.yaml`.

## Inference

```bash
python tools/model-canonicalizer/predict.py \
  --model zhiheng-qian/etc-qwen3.5-4b \
  --input /path/to/input.jsonl \
  --out predictions.jsonl \
  --device auto \
  --batch-size 16
```

The input schema is `{id, language, text}`. The output schema is `{id, canonical_text, status, error}` and is shared with TACS.

The bundled `prompt.txt` is the exact system prompt used by the released checkpoints at training and inference time. It is intentionally preserved verbatim for reproducibility, including its original terminology.

`torch_npu` and the CANN runtime are required only for Ascend NPU inference. CUDA and CPU inference do not import `torch_npu` as a hard dependency.

