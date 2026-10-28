# zh canonical contracts

This file declares exact `C(zh, category, phenomenon)` contracts. The ISO 639-1 filename identifies the language. Follow `../canonicalization-method.md`.

Conventions: metalanguage and schema keys are English; `category`/`phenomenon` are benchmark identifiers; canonical literals are written in the target-language script (Simplified Chinese here) exactly as the agent should output them. Each `instruction` states the canonical (annotation) form of the phenomenon; it does not enumerate benchmark material or transcription-dependent cases. Category methodology never supplies a rendering fallback; without an exact applicable contract, retain the source span.

Shared rendering conventions:

```yaml
numeric_digits: ASCII 0-9
decimal_separator: "."
negative_sign: "-"
canonical_han_script: Simplified Chinese
latin_width: halfwidth
identifier_latin_case: uppercase
phonetic_transcription:
  language: Standard Mandarin
  representation: broad IPA
  tone: lexical tone
  tone_sandhi: excluded
  syllable_separator: single ASCII space
  wrapper: "/.../"
```

Canonical rendering may depend on the recovered semantic value and context inside the current record, but never on the source-side spelling, separator, symbol-versus-name choice, or another batch record.

## orthographic_variants

- category: orthographic_variants
  phenomenon: simplified_traditional
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span in normative Simplified Chinese. Resolve
      one-to-many character conversions from the complete lexical context;
      if no unique same-meaning Simplified form is recoverable, retain the
      source span.
- category: orthographic_variants
  phenomenon: variant_characters
  canonical_form:
    type: generative
    instruction: >
      Render the accepted character with its standard character form —
      the standard Simplified Chinese character for the recovered
      character. Variant forms converge to the standard form, e.g.
      峯 → 峰, 汙 → 污, 羣 → 群, 菸 → 烟.
- category: orthographic_variants
  phenomenon: heterographic_words
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the standard written form of the
      recovered word given by the normative heterographic-word standard
      《第一批异形词整理表》; nonstandard spelling variants converge to
      the standard form, e.g. 刻划 → 刻画, 勾划 → 勾画, 联接 → 连接,
      连结 → 联结, 简炼 → 简练, 涵义 → 含义.
- category: orthographic_variants
  phenomenon: financial_capital_numerals
  canonical_form:
    type: generative
    instruction: >
      Recover the complete numeric value and render it with ASCII Arabic
      digits under the shared numeric conventions. Financial capital,
      ordinary CJK, and Arabic representations of the same quantity converge
      to the same digit string.
- category: orthographic_variants
  phenomenon: zero_character_variants
  canonical_form:
    type: generative
    instruction: >
      A zero digit inside a digit-by-digit CJK numeral string (years, room
      numbers, identifiers) is written 「〇」. A 零 standing for such a zero
      digit converges to 〇; the measure-word zero of a quantity is not this
      phenomenon.
## homophonic_substitutions

- category: homophonic_substitutions
  phenomenon: homophonic_names
  canonical_form:
    type: generative
    instruction: >
      Render the complete name's contextually determined Standard Mandarin
      pronunciation in broad IPA under the shared phonetic conventions.
      Different written names converge only when their complete pronunciations
      are identical. If the pronunciation cannot be determined from the
      current record, retain the source span.
- category: homophonic_substitutions
  phenomenon: third_person_pronoun_script_variants
  canonical_form:
    type: generative
    instruction: >
      Render the pronoun's Standard Mandarin pronunciation in broad IPA under
      the shared phonetic conventions. 他, 她, and 它 therefore converge to
      /tʰa˥/ when pronounced tā.
- category: homophonic_substitutions
  phenomenon: surname_script_variants
  canonical_form:
    type: generative
    instruction: >
      Render the complete surname's contextually determined Standard Mandarin
      pronunciation in broad IPA under the shared phonetic conventions.
      Same-reading surname spellings converge only when their complete
      pronunciations are identical. If the reading is ambiguous, retain the
      source span.
- category: homophonic_substitutions
  phenomenon: common_word_homophones
  canonical_form:
    type: generative
    instruction: >
      Render the complete word's contextually determined Standard Mandarin
      pronunciation in broad IPA under the shared phonetic conventions.
      Resolve polyphonic characters only from context inside the current
      record. Different written words converge only when their complete
      pronunciations, including lexical tones, are identical; otherwise retain
      the source span.
## numeric_expressions

- category: numeric_expressions
  phenomenon: cardinal
  canonical_form:
    type: generative
    instruction: >
      Quantities are written with Arabic numerals.
- category: numeric_expressions
  phenomenon: ordinal
  canonical_form:
    type: generative
    instruction: >
      Ranks are written with Arabic numerals, keeping the ordinal prefix
      「第」.
- category: numeric_expressions
  phenomenon: decimal
  canonical_form:
    type: generative
    instruction: >
      Decimal values are written with Arabic numerals and 「.」 as the decimal
      separator, preserving sign, digits, and written precision.
- category: numeric_expressions
  phenomenon: fraction
  canonical_form:
    type: generative
    instruction: >
      Simple fractions are written as an ASCII Arabic numerator and denominator
      joined by 「/」. Mixed numbers are written as an integer, one ASCII space,
      and the unreduced fractional part. Preserve the explicitly expressed
      numerator and denominator; do not reduce the fraction or convert it to a
      decimal.
- category: numeric_expressions
  phenomenon: date
  canonical_form:
    type: generative
    instruction: >
      Complete Gregorian dates are written as YYYY年M月D日 with ASCII Arabic
      digits. The year has four digits; month and day have no leading zero.
      Do not infer an unexpressed century or missing field.
- category: numeric_expressions
  phenomenon: time
  canonical_form:
    type: generative
    instruction: >
      Clock times with expressed minutes are written in 24-hour HH:MM form
      using ASCII digits and 「:」. Resolve an expressed period-of-day word into
      the 24-hour value and omit that word from the canonical form. When only
      an hour is expressed, write the Arabic hour without inventing minutes.
- category: numeric_expressions
  phenomenon: currency
  canonical_form:
    type: generative
    instruction: >
      Monetary amounts are written as an ASCII Arabic amount followed by the
      canonical Simplified Chinese currency name determined from the recovered
      currency identity. Symbol, abbreviation, and spoken-name inputs for the
      same currency converge to that same currency name. Preserve explicitly
      expressed fractional precision.
- category: numeric_expressions
  phenomenon: unit
  canonical_form:
    type: generative
    instruction: >
      Measured values are written as an ASCII Arabic number followed by the
      canonical Simplified Chinese unit name for the recovered unit identity.
      Symbols, abbreviations, and synonymous spoken unit names converge to the
      same unit name. Use no space between the number and a Chinese unit name.
- category: numeric_expressions
  phenomenon: phone
  canonical_form:
    type: generative
    instruction: >
      Telephone numbers are written as one contiguous ASCII digit string with
      all presentation grouping separators removed. Preserve a leading
      international 「+」 when it is part of the recovered number. A digit
      spelled in CJK characters, including 幺 for 1, is rendered as its Arabic
      digit.
- category: numeric_expressions
  phenomenon: roman
  canonical_form:
    type: generative
    instruction: >
      A value conventionally expressed with Roman numerals is written in
      normalized uppercase Roman-numeral notation using I, V, X, L, C, D, M.
      Arabic, CJK, lowercase Roman, and uppercase Roman inputs with the same
      value converge to the same minimal standard Roman numeral.
- category: numeric_expressions
  phenomenon: sports_score
  canonical_form:
    type: generative
    instruction: >
      A competition score is written as two ASCII Arabic numbers joined by the
      ASCII hyphen-minus 「-」 in competitor order, independent of the source
      separator.
## symbols_markers

- category: symbols_markers
  phenomenon: address
  canonical_form:
    type: generative
    instruction: >
      Numeric address components are written with ASCII Arabic digits followed
      by the canonical Simplified Chinese marker for their recovered address
      role, such as 号、栋、单元、室. Spoken and abbreviated realizations of the
      same role converge to that marker.
- category: symbols_markers
  phenomenon: biological
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic zh canonical rendering is declared for
      biological names or notation. Retain the source span unchanged.
- category: symbols_markers
  phenomenon: chemical
  canonical_form:
    type: generative
    instruction: >
      Chemical formulas are written with element symbols and subscript atom
      counts.
- category: symbols_markers
  phenomenon: coordinates
  canonical_form:
    type: generative
    instruction: >
      Geographic coordinates are written with ASCII Arabic numerals and the
      symbols 「°」「′」「″」 for expressed degree, minute, and second fields.
      Direction is written as uppercase N, S, E, or W. Spoken and symbolic
      inputs with the same coordinate value converge to this notation.
- category: symbols_markers
  phenomenon: hashtag
  canonical_form:
    type: generative
    instruction: >
      A hashtag is written with 「#」 and a mention with 「@」, immediately
      followed by the recovered tag or handle text. Spoken marker names and
      symbol inputs converge to the corresponding ASCII marker.
- category: symbols_markers
  phenomenon: isbn
  canonical_form:
    type: generative
    instruction: >
      The identifier is written as the uppercase prefix 「ISBN」 followed by
      one ASCII space and then a contiguous ISBN-10 or ISBN-13 character
      string. Remove presentation spaces and hyphens inside the identifier;
      write an ISBN-10 check character as uppercase X.
- category: symbols_markers
  phenomenon: legal
  canonical_form:
    type: generative
    instruction: >
      Render each recovered case number or legal citation in its conventional
      Simplified Chinese written template. Use ASCII Arabic digits, halfwidth
      uppercase Latin letters, and the canonical structural separator required
      by the recovered citation type; spoken separator names and typographic
      variants converge to that separator.
- category: symbols_markers
  phenomenon: license
  canonical_form:
    type: generative
    instruction: >
      License plates and serial numbers are written as contiguous halfwidth
      alphanumeric strings. Use uppercase Latin letters and ASCII digits, and
      remove presentation spaces and separators that are not part of the
      identifier's semantic value.
- category: symbols_markers
  phenomenon: math
  canonical_form:
    type: generative
    instruction: >
      Mathematical expressions are written with ASCII Arabic numerals and the
      canonical symbols +, -, ×, ÷, =, <, >, %, and parentheses for the
      recovered operators and grouping. Spoken operator names and typographic
      variants converge to these symbols. Preserve the original expression
      tree and explicitly expressed grouping.
- category: symbols_markers
  phenomenon: musical
  canonical_form:
    type: retain
    reason: >
      No single deterministic rendering is declared for the different kinds
      of musical notation covered by this phenomenon. Retain the source span
      until subtype-specific contracts are defined.
- category: symbols_markers
  phenomenon: stock
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic zh canonical rendering is declared for
      stock tickers or market-qualified symbols. Retain the source span
      unchanged.
- category: symbols_markers
  phenomenon: url
  canonical_form:
    type: generative
    instruction: >
      URLs and email addresses are written contiguously in their recovered
      address form. Render spoken separator names as the corresponding ASCII
      characters such as @, ., /, :, ?, =, &, and -. Preserve letter case only
      where it is semantically significant; do not copy presentation spacing.
- category: symbols_markers
  phenomenon: vehicle
  canonical_form:
    type: generative
    instruction: >
      Model and product codes are written as contiguous halfwidth alphanumeric
      strings using uppercase Latin letters and ASCII digits. Retain only a
      separator that belongs to the recovered code identity; remove purely
      presentational spacing or grouping.
- category: symbols_markers
  phenomenon: version
  canonical_form:
    type: generative
    instruction: >
      Version identifiers are written as Arabic digit components separated by
      「.」.
