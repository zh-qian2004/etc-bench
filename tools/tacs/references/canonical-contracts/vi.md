# vi canonical contracts

This file declares exact `C(vi, category, phenomenon)` contracts. The ISO 639-1 filename identifies the language. Follow `../canonicalization-method.md`.

Conventions: metalanguage and schema keys are English; `category`/`phenomenon` are benchmark identifiers; canonical literals are written in Standard Vietnamese exactly as the agent should output them. Each `instruction` states the canonical form of the phenomenon; it does not enumerate benchmark material or transcription-dependent cases. Category methodology never supplies a rendering fallback; without an exact applicable contract, retain the source span.

Shared rendering conventions:

```yaml
numeric_digits: ASCII 0-9
decimal_separator: "," (comma)
negative_sign: "-"
vietnamese_orthography: Standard Vietnamese, current national norm
latin_width: halfwidth
identifier_latin_case: lowercase for natural-language words
phonetic_transcription:
  language: Standard Vietnamese (Hanoi norm)
  representation: broad phonemic IPA
  tone: all six tones marked (phonemic)
  vowel_length: not marked (non-phonemic)
  stress: not marked (syllable-timed, non-phonemic)
  dialect_condition: regional mergers (tr/ch, s/x) are transcribed merged
    only where the phenomenon explicitly declares them
  connected_speech: no cross-word sandhi
  syllable_separator: single ASCII space
  wrapper: "/.../"
```

Canonical rendering may depend on the recovered semantic value and context inside the current record, but never on the source-side spelling, separator, symbol-versus-name choice, or another batch record.

## orthographic_variants

- category: orthographic_variants
  phenomenon: postconsonantal_i_y_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted syllable with the letter y for the postconsonantal
      /i/ nucleus, e.g. lý, kỹ, mỹ, hy vọng, công ty. The i spelling of
      the same syllable converges to the y form.
- category: orthographic_variants
  phenomenon: qu_i_y_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted syllable with y after qu, e.g. quý, quỷ, quỹ.
      The i spelling of the same syllable converges to the y form.
- category: orthographic_variants
  phenomenon: oa_tone_mark_position_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted open oa syllable with the tone mark on the a,
      e.g. hoà, toả, hoạ. The o-marked spelling of the same syllable
      converges to the a-marked form.
- category: orthographic_variants
  phenomenon: oe_tone_mark_position_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted open oe syllable with the tone mark on the e,
      e.g. khoẻ, xoè, loé. The o-marked spelling of the same syllable
      converges to the e-marked form.
- category: orthographic_variants
  phenomenon: uy_tone_mark_position_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted open uy syllable with the tone mark on the y,
      e.g. thuỷ, tuỳ, huỷ. The u-marked spelling of the same syllable
      converges to the y-marked form.
- category: orthographic_variants
  phenomenon: d_gi_lexical_spelling_doublets
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word of a d/gi lexical doublet with the gi-
      spelling of the recovered word; the d- spelling of the same word
      converges to the gi- form, e.g. dông → giông, dẫm → giẫm, dúi →
      giúi.
- category: orthographic_variants
  phenomenon: loanword_hyphen_space_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted syllabified loanword with single ASCII spaces
      between its syllables, e.g. ô tô, sô cô la, mít tinh. The
      hyphenated spelling of the same loanword converges to the
      space-separated form.
- category: orthographic_variants
  phenomenon: loanword_hyphen_solid_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted scientific and international loanword as one
      solid word, e.g. kilôgam, milimét, đêximét. The hyphenated
      syllable-by-syllable spelling of the same loanword converges to
      the solid form.
- category: orthographic_variants
  phenomenon: international_vs_vietnamized_loan_spelling
  canonical_form:
    type: generative
    instruction: >
      Render the accepted loanword in its Vietnamized (transcribed)
      spelling, e.g. ra-đi-ô, ra-đa, la-de, ca-mê-ra. The international
      spelling of the same loanword converges to the Vietnamized form.
## homophonic_substitutions

- category: homophonic_substitutions
  phenomenon: i_y_orthographic_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      tone marked. The i and y spellings of the same name syllable
      converge, e.g. Lý and Lí → /li˨˩˦/, Mỹ and Mĩ → /mi˧˥/, Tý and
      Tí → /ti˨˩˦/. If the reading cannot be determined, retain the
      source span.
- category: homophonic_substitutions
  phenomenon: tr_ch_regional_merger
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      tone marked and the southern merged retroflex onset transcribed
      /tɕ/, e.g. Trinh and Chinh → /tɕiŋ˧/, Trung and Chung →
      /tɕuŋ˧/. If the record clearly expresses a distinction between tr
      /ʈ/ and ch /tɕ/, transcribe that distinction instead; otherwise,
      if the reading cannot be determined, retain the source span.
- category: homophonic_substitutions
  phenomenon: s_x_regional_merger
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      tone marked and the southern merged sibilant transcribed /s/, e.g.
      Sương and Xương → /sɨəŋ˧/, Sinh and Xinh → /siŋ˧/. If the record
      clearly distinguishes /ʂ/ from /s/, transcribe that distinction
      instead; otherwise, if the reading cannot be determined, retain
      the source span.
- category: homophonic_substitutions
  phenomenon: foreign_name_vietnamese_reading_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted foreign name's Vietnamese reading in broad
      phonemic IPA under the shared phonetic conventions, with tone
      marked, e.g. Li, Lee, and Lý converge to /li˨˩˦/ as read in
      Vietnamese; Chen converges to its Vietnamese reading /tɕən˧/.
      Never transcribe the original-language pronunciation. If the
      reading cannot be determined, retain the source span.
## numeric_expressions

- category: numeric_expressions
  phenomenon: cardinal
  canonical_form:
    type: generative
    instruction: >
      Quantities are written with ASCII digits. Spelled-out Vietnamese
      number words and digits for the same quantity converge to the same
      ASCII digit string.
- category: numeric_expressions
  phenomenon: ordinal
  canonical_form:
    type: generative
    instruction: >
      Ranks are written with ASCII digits; the Vietnamese ordinal form
      (thứ + number word) of the same rank converges to the bare digit
      string of the rank value.
- category: numeric_expressions
  phenomenon: decimal
  canonical_form:
    type: generative
    instruction: >
      Decimal values are written with ASCII digits and 「,」 (comma) as
      the decimal separator, preserving sign, digits, and written
      precision. Point-separated writings of the same value converge
      to the comma form.
- category: numeric_expressions
  phenomenon: fraction
  canonical_form:
    type: generative
    instruction: >
      Simple fractions are written as an ASCII numerator and
      denominator joined by 「/」. Mixed numbers are written as an
      integer, one ASCII space, and the unreduced fractional part.
      Preserve the explicitly expressed numerator and denominator; do
      not reduce the fraction or convert it to a decimal.
- category: numeric_expressions
  phenomenon: date
  canonical_form:
    type: generative
    instruction: >
      Complete dates are written as D/M/YYYY with ASCII digits, the day
      and month with no leading zero, and a four-digit year, e.g.
      3/7/2026. Spelled-out dates converge to this numeric form. Do not
      infer an unexpressed century or missing field.
- category: numeric_expressions
  phenomenon: time
  canonical_form:
    type: generative
    instruction: >
      Clock times with expressed minutes are written in 24-hour HH:MM
      form using ASCII digits and 「:」. Resolve an expressed period-of-day
      word such as sáng, trưa, chiều, tối, or đêm into the 24-hour
      value and omit that word from the canonical form. When only an
      hour is expressed, write the hour number alone without inventing
      minutes.
- category: numeric_expressions
  phenomenon: currency
  canonical_form:
    type: generative
    instruction: >
      Monetary amounts are written as an ASCII digit amount, one ASCII
      space, and the canonical Vietnamese name of the recovered
      currency identity (đồng for the Vietnamese dong, đô la for the
      US dollar, euro for the euro, with a qualifier when the bare name
      is ambiguous, e.g. đô la Singapore). Symbol, abbreviation, and
      spoken-name inputs for the same currency converge to that name.
      Preserve explicitly expressed fractional precision.
- category: numeric_expressions
  phenomenon: unit
  canonical_form:
    type: generative
    instruction: >
      Measured values are written as an ASCII digit number, one ASCII
      space, and the canonical Vietnamese name of the recovered unit
      identity (e.g. ki-lô-mét or kilômét per the orthographic
      contract, mét, xen-ti-mét, ki-lô-gam, gam, lít, mi-li-lít, độ
      C). Symbols, abbreviations, and synonymous spoken unit names
      converge to the same unit name.
- category: numeric_expressions
  phenomenon: phone
  canonical_form:
    type: generative
    instruction: >
      Telephone numbers are written as one contiguous ASCII digit string
      with all presentation grouping separators removed. Preserve a
      leading international 「+」 when it is part of the recovered
      number.
- category: numeric_expressions
  phenomenon: roman
  canonical_form:
    type: generative
    instruction: >
      A value conventionally expressed with Roman numerals is written
      in normalized uppercase Roman-numeral notation using I, V, X, L,
      C, D, M. Spelled Vietnamese, lowercase Roman, and uppercase Roman
      inputs with the same value converge to the same minimal standard
      Roman numeral.
- category: numeric_expressions
  phenomenon: sports_score
  canonical_form:
    type: generative
    instruction: >
      A competition score is written as two ASCII digit numbers joined
      by the ASCII hyphen-minus 「-」 in competitor order, independent of
      the source separator.
## symbols_markers

- category: symbols_markers
  phenomenon: address
  canonical_form:
    type: generative
    instruction: >
      Numeric address components are written with ASCII digits followed
      by the canonical Vietnamese marker for their recovered address
      role, such as đường, số, ngõ, tổ, phường, xã, tầng. Spoken and
      abbreviated realizations of the same role converge to that
      marker.
- category: symbols_markers
  phenomenon: biological
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic vi canonical rendering is
      declared for biological names or notation. Retain the source span
      unchanged.
- category: symbols_markers
  phenomenon: chemical
  canonical_form:
    type: generative
    instruction: >
      Chemical formulas are written with halfwidth Latin element symbols
      and ASCII digit atom counts attached directly, e.g. H2O, CO2,
      preserving the recovered element sequence.
- category: symbols_markers
  phenomenon: coordinates
  canonical_form:
    type: generative
    instruction: >
      Geographic coordinates are written with ASCII digits and the
      symbols 「°」「′」「″」 for expressed degree, minute, and second
      fields. Direction is written as uppercase N, S, E, or W. Spoken
      and symbolic inputs with the same coordinate value converge to
      this notation.
- category: symbols_markers
  phenomenon: hashtag
  canonical_form:
    type: generative
    instruction: >
      A hashtag is written with 「#」 and a mention with 「@」, immediately
      followed by the recovered tag or handle text. Spoken marker names
      and symbol inputs converge to the corresponding ASCII marker.
- category: symbols_markers
  phenomenon: isbn
  canonical_form:
    type: generative
    instruction: >
      The identifier is written as the uppercase prefix 「ISBN」 followed
      by one ASCII space and then a contiguous ISBN-10 or ISBN-13
      character string. Remove presentation spaces and hyphens inside
      the identifier; write an ISBN-10 check character as uppercase X.
- category: symbols_markers
  phenomenon: legal
  canonical_form:
    type: generative
    instruction: >
      Render each recovered legal citation element in its conventional
      Vietnamese written template, using the canonical structural
      label of the recovered citation type (e.g. Điều, Khoản, Luật),
      ASCII digits, and halfwidth uppercase Latin letters where the
      citation contains them. Typographic variants converge to the
      canonical template.
- category: symbols_markers
  phenomenon: license
  canonical_form:
    type: generative
    instruction: >
      License plates and serial numbers are written as contiguous
      halfwidth alphanumeric strings. Use uppercase Latin letters and
      ASCII digits, and remove presentation spaces and separators that
      are not part of the identifier's semantic value.
- category: symbols_markers
  phenomenon: math
  canonical_form:
    type: generative
    instruction: >
      Mathematical expressions are written with ASCII digits and the
      canonical symbols +, -, ×, ÷, =, <, >, %, and parentheses for the
      recovered operators and grouping. Spoken operator names and
      typographic variants converge to these symbols. Preserve the
      original expression tree and explicitly expressed grouping.
- category: symbols_markers
  phenomenon: musical
  canonical_form:
    type: retain
    reason: >
      No single deterministic rendering is declared for the different
      kinds of musical notation covered by this phenomenon. Retain the
      source span until subtype-specific contracts are defined.
- category: symbols_markers
  phenomenon: stock
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic vi canonical rendering is
      declared for stock tickers or market-qualified symbols. Retain the
      source span unchanged.
- category: symbols_markers
  phenomenon: url
  canonical_form:
    type: generative
    instruction: >
      URLs and email addresses are written contiguously in their
      recovered address form. Render spoken separator names as the
      corresponding ASCII characters such as @, ., /, :, ?, =, &, and -.
      Preserve letter case only where it is semantically significant; do
      not copy presentation spacing.
- category: symbols_markers
  phenomenon: vehicle
  canonical_form:
    type: generative
    instruction: >
      Model and product codes are written as contiguous halfwidth
      alphanumeric strings using uppercase Latin letters and ASCII
      digits. Retain only a separator that belongs to the recovered
      code identity; remove purely presentational spacing or grouping.
- category: symbols_markers
  phenomenon: version
  canonical_form:
    type: generative
    instruction: >
      Version identifiers are written as ASCII digit components
      separated by 「.」.
