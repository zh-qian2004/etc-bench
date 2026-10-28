"""Greedy batched inference for the released ETC canonicalizers."""
from __future__ import annotations

import importlib.machinery
import os
import sys
import types
from pathlib import Path
from typing import Callable

os.environ.setdefault("TORCH_DEVICE_BACKEND_AUTOLOAD", "0")

import torch

try:  # Registers the optional Ascend backend when CANN is configured.
    import torch_npu  # noqa: F401
except Exception:  # pragma: no cover - optional backend is unusable
    sys.modules.pop("torch_npu", None)
    mock_npu = types.ModuleType("torch_npu")
    mock_npu.__path__ = []
    mock_npu.__spec__ = importlib.machinery.ModuleSpec("torch_npu", None)
    mock_npu.npu = types.ModuleType("torch_npu.npu")
    mock_npu.npu.__spec__ = importlib.machinery.ModuleSpec("torch_npu.npu", None)
    sys.modules["torch_npu"] = mock_npu
    sys.modules["torch_npu.npu"] = mock_npu.npu

from transformers import AutoModelForCausalLM, AutoTokenizer


SYSTEM_PROMPT = (Path(__file__).with_name("prompt.txt")
                 .read_text(encoding="utf-8").strip())


def resolve_device(device: str) -> str:
    if device != "auto":
        return device
    if torch.cuda.is_available():
        return "cuda"
    if hasattr(torch, "npu") and torch.npu.is_available():
        return "npu:0"
    return "cpu"


def resolve_dtype(name: str, device: str):
    if name == "auto":
        return torch.float32 if device == "cpu" else torch.bfloat16
    choices = {
        "float32": torch.float32,
        "float16": torch.float16,
        "bfloat16": torch.bfloat16,
    }
    if name not in choices:
        raise ValueError(f"unsupported dtype: {name}")
    return choices[name]


def load_canonicalizer(model_id: str, device: str = "auto", dtype: str = "auto"):
    device = resolve_device(device)
    torch_dtype = resolve_dtype(dtype, device)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    template = Path(model_id) / "chat_template.jinja"
    if template.exists():
        tokenizer.chat_template = template.read_text(encoding="utf-8")
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch_dtype)
    model.config.use_cache = True
    model.to(device)
    model.eval()
    return tokenizer, model, device


def build_prompts(tokenizer, texts: list[str]) -> list[str]:
    return [
        tokenizer.apply_chat_template(
            [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text},
            ],
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,
        )
        for text in texts
    ]


@torch.no_grad()
def generate(
    tokenizer,
    model,
    texts: list[str],
    device: str,
    batch_size: int = 16,
    max_new_tokens: int = 256,
    on_progress: Callable[[int, int], None] | None = None,
) -> list[str]:
    """Greedily decode one canonical text for every input text."""
    if not texts:
        return []
    outputs: list[str | None] = [None] * len(texts)
    encoded = [
        tokenizer(prompt, add_special_tokens=False)["input_ids"]
        for prompt in build_prompts(tokenizer, texts)
    ]
    order = sorted(range(len(encoded)), key=lambda index: len(encoded[index]))

    for start in range(0, len(order), batch_size):
        indices = order[start:start + batch_size]
        sequences = [encoded[index] for index in indices]
        width = max(len(sequence) for sequence in sequences)
        input_ids, attention_mask = [], []
        for sequence in sequences:
            padding = width - len(sequence)
            input_ids.append([tokenizer.pad_token_id] * padding + sequence)
            attention_mask.append([0] * padding + [1] * len(sequence))

        ids = torch.tensor(input_ids, dtype=torch.long, device=device)
        mask = torch.tensor(attention_mask, dtype=torch.long, device=device)
        generated = model.generate(
            input_ids=ids,
            attention_mask=mask,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )
        for row, index in enumerate(indices):
            outputs[index] = tokenizer.decode(
                generated[row, ids.shape[1]:], skip_special_tokens=True
            ).strip()
        if on_progress:
            on_progress(min(start + batch_size, len(order)), len(order))

    return [output if output is not None else "" for output in outputs]

