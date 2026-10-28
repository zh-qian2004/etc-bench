# Batch trace sidecar contract

Create a UTF-8 JSONL trace sidecar only when explicitly requested. It has exactly one record per successful canonical output, in the same order and keyed by the same ID:

```json
{"id":"opaque-unique-id","edits":[{"quote":"10 km","occurrence":1,"category":"numeric_expressions","phenomenon":"unit","semantic_value":{"quantity":10,"unit":"kilometre"},"replacement":"ten kilometers","confidence":"high"}]}
```

Requirements:

- `occurrence` is one-based among exact matches of `quote` in that record's input text.
- `quote` is copied exactly, including case and internal whitespace.
- `semantic_value` exposes the value used to render the replacement.
- Emit only committed edits. Do not emit rejected candidates or no-op edits.
- `confidence` is `high`; uncertain edits are omitted.
- Edits resolve to distinct, non-overlapping spans.
- Applying the edits from right to left must reproduce `canonical_text` exactly.
- Trace generation failure must not corrupt the canonical output file.

The trace records agent decisions. A validator may check structure and reconstruction but must not decide or generate canonical text.

