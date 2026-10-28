# Canonicalization method

Use this procedure internally for one `(text, language)` input. In the JSON interface, the `language` field supplies its ISO 639-1 code.

## 1. Candidate discovery

Scan the text against the loaded inventory. A candidate must have exact source evidence and an inventory label. Recognize semantic objects, not merely visual patterns: a digit string may be a cardinal, date, time, identifier, score, version, or telephone number.

Do not treat ordinary spelling correction, grammar repair, punctuation cleanup, translation, or stylistic rewriting as ETC canonicalization.

## 2. Applicability and span resolution

For each candidate, test the phenomenon description, its context/applicability note, and exclusions. Prefer a specialized phenomenon that covers the complete semantic object over a generic phenomenon covering a subpart.

Accepted edits must not overlap. If two analyses compete:

1. prefer the analysis preserving the most complete structured value;
2. otherwise prefer the more specific phenomenon over a generic numeric or symbol subpart;
3. if still ambiguous, make no edit.

The span includes every character required to render the object canonically, but excludes surrounding syntax that is not part of it.

## 3. Recover semantic value

Represent what the span means before deciding how it should look. Preserve all meaningful fields. Typical values include:

- numeric: sign, integer/fractional value, scale, precision, role;
- date/time: calendar fields, ordering, period, timezone;
- unit/currency: amount, unit, currency, grammatical number;
- identifiers: complete ordered digits/letters and grouping role;
- abbreviation: intended expansion selected by context;
- orthography: lexical item or character plus equivalence group;
- homophony: pronunciation/equivalence group and the contextually intended lexical item.

If the value cannot be recovered confidently, do not edit.

## 4. Resolve and apply the canonical contract

Look up the exact contract `C(language, category, phenomenon)` in `references/canonical-contracts/{language}.md`. The matching file in `references/taxonomy/languages/` contains only the phenomenon inventory. The `language` field is an ISO 639-1 code and an index into the contract registry. Category guidance helps recognize the phenomenon and recover its semantic value; it never determines the output form.

After the phenomenon and span have already been accepted, apply a replacement only when the exact contract exists and determines an unambiguous rendering. Otherwise retain the source span. Do not invent a canonical form from model knowledge, a category default, or a general regional convention.

A contract only maps the recovered semantic value and permitted local context to a canonical string. Recognition, applicability, span selection, overlap resolution, and semantic preservation belong to the taxonomy, this method, and the global invariants—not to the contract. A contract may specify a fixed surface, a generative natural-language rendering instruction, or `retain`.

Author contracts in `references/canonical-contracts/{language}.md` with this declarative shape:

```yaml
- category: <inventory category>
  phenomenon: <inventory phenomenon>
  canonical_form:
    type: fixed
    value: <one literal target>
```

```yaml
- category: <inventory category>
  phenomenon: <inventory phenomenon>
  canonical_form:
    type: generative
    instruction: <mapping from recovered semantic value to output string>
```

```yaml
- category: <inventory category>
  phenomenon: <inventory phenomenon>
  canonical_form:
    type: retain
    reason: <why this solver intentionally retains the accepted span>
```

The contract filename supplies the BCP-tagged language identifier, so each entry denotes exactly one `C(language, category, phenomenon)`. `category` and `phenomenon` must match the corresponding closed inventory in `references/taxonomy/languages/{language}.md` or the language-agnostic inventory. `fixed` requires `value`, `generative` requires `instruction`, and `retain` requires `reason`; do not mix these payload fields. This is an agent-facing declarative contract, not an executable rewrite program or benchmark-derived mapping.

### Numeric expressions and symbols/markers

When the exact contract requests a spoken rendering, retain every meaningful component; do not summarize or use placeholders. Follow its instructions for identifier reading, spacing, punctuation, and grammatical realization.

Identifiers are usually read component-by-component rather than as a quantity. Dates, times, fractions, scores, versions, and addresses follow their semantic role rather than the cardinal rule.

### Abbreviations

Recover the contextually intended expansion for contract matching. Expand or stabilize the abbreviation only as the exact contract directs. Ambiguity means no edit.

### Orthographic variants

Map equivalent spellings only to the target declared by the exact contract. If no target is declared, retain the source even when the model knows a common regional standard.

### Homophonic substitutions

Do not merge arbitrary homophones merely because pronunciation matches. Apply only inventory-defined equivalence groups under their stated applicability and only when the exact contract declares the canonical surface. Without that contract, retain the source.

## 5. Commit local edits

Copy the source exactly and replace only accepted spans. Apply multiple replacements from right to left by source position. Recheck that:

- every replacement follows from its recovered value;
- no meaningful component disappeared;
- edits do not overlap;
- all text outside edits is byte-for-byte unchanged;
- the result contains no analysis markup.

Conservatism applies per span: uncertainty about one span does not block other independent, confident edits.
