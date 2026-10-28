# ar canonical contracts

This file declares exact `C(ar, category, phenomenon)` contracts. The ISO 639-1 filename identifies the language. Follow `../canonicalization-method.md`.

Conventions: metalanguage and schema keys are English; `category`/`phenomenon` are benchmark identifiers; canonical literals are written in Modern Standard Arabic (Saudi written norm) exactly as the agent should output them. Each `instruction` states the canonical form of the phenomenon; it does not enumerate benchmark material or transcription-dependent cases. Category methodology never supplies a rendering fallback; without an exact applicable contract, retain the source span.

Shared rendering conventions:

```yaml
numeric_digits: ASCII 0-9; Eastern Arabic-Indic digits converge to ASCII digits
decimal_separator: "."
negative_sign: "-"
arabic_script: Modern Standard Arabic, Saudi written norm
latin_width: halfwidth
identifier_latin_case: uppercase
phonetic_transcription:
  language: Modern Standard Arabic, Saudi broadcast/recitation norm
  representation: broad phonemic IPA
  vowel_length: marked (phonemic)
  tone: not applicable
  stress: not marked (predictable, non-phonemic)
  connected_speech: only word-internal definite-article assimilation is applied; no cross-word sandhi
  word_separator: single ASCII space
  wrapper: "/.../"
```

Canonical rendering may depend on the recovered semantic value and context inside the current record, but never on the source-side spelling, separator, symbol-versus-name choice, or another batch record.

## orthographic_variants

- category: orthographic_variants
  phenomenon: diacritic_presence_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word in its unvocalized modern standard form:
      remove every optional tashkīl mark (fatḥa, ḍamma, kasra, sukūn,
      shadda, tanwīn), leaving the base letters, all hamza forms, and
      madda untouched. Fully vocalized, partially vocalized, and bare
      writings of the same word converge to the same bare skeleton.
- category: orthographic_variants
  phenomenon: hamza_seat_variants
  canonical_form:
    type: generative
    instruction: >
      Render the word with the seat required by the standard hamza rule
      for its recovered pronunciation: a medial hamza sits on the letter
      of the strongest vowel among the preceding vowel and the hamza's
      own vowel, ordered kasra over ḍamma over fatḥa (kasra → ئ, ḍamma →
      ؤ, otherwise أ); word-initial and word-final hamza keep their
      normative seats. Variant spellings of one word converge to the
      rule-selected spelling. If the word is an established
      orthographic exception or the rule yields no unique seat, retain
      the source span.
- category: orthographic_variants
  phenomenon: uthmani_imla_i_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted Quranic or religious span in modern standard
      orthography (al-rasm al-imlāʾī): use the modern letter choices of
      the same word, such as الصلاة and الزكاة with alif, and remove
      Uthmani-only devices such as the superscript alef of هٰذا. If the
      modern standard spelling of the word cannot be determined, retain
      the source span.
- category: orthographic_variants
  phenomenon: proper_name_compound_spacing
  canonical_form:
    type: generative
    instruction: >
      Render the compound personal name with the first component عبد
      as a separate word followed by one ASCII space and the remaining
      component, e.g. عبد الله, عبد الرحمن. Joined and spaced writings
      of the same name converge to the spaced form.
## homophonic_substitutions

- category: homophonic_substitutions
  phenomenon: final_alif_maqsura_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. A
      word-final /aː/ is transcribed the same way whether written with
      ا or ى, so علا and على converge to /ʕalaː/. If the intended
      reading cannot be determined from the current record, retain the
      source span.
- category: homophonic_substitutions
  phenomenon: hamza_seat_orthographic_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's pronunciation in broad phonemic IPA
      under the shared phonetic conventions. The glottal stop is
      transcribed /ʔ/ whatever its written seat, so مئة and مائة
      converge to /miʔa/ and مسؤول and مسئول converge to /masʔuːl/.
      If the reading cannot be determined, retain the source span.
- category: homophonic_substitutions
  phenomenon: proper_name_common_noun_homophones
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      name reading and the common-noun reading of the same phonological
      word, such as حسن, converge to /ħasan/. If the reading cannot be
      determined from the current record, retain the source span.
- category: homophonic_substitutions
  phenomenon: proper_name_verb_homophones
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      name reading and the verb reading of the same phonological word,
      such as يحيى, converge to /jaħjaː/. If the reading cannot be
      determined, retain the source span.
## numeric_expressions

- category: numeric_expressions
  phenomenon: cardinal
  canonical_form:
    type: generative
    instruction: >
      Quantities are written with ASCII digits. Spelled-out Arabic
      number words, Eastern Arabic-Indic digits, and ASCII digits for
      the same quantity converge to the same ASCII digit string.
- category: numeric_expressions
  phenomenon: ordinal
  canonical_form:
    type: generative
    instruction: >
      Ranks are written with ASCII digits; the ordinal word, its
      definite article, and digit writings of the same rank converge to
      the bare digit string of the rank value.
- category: numeric_expressions
  phenomenon: decimal
  canonical_form:
    type: generative
    instruction: >
      Decimal values are written with ASCII digits and 「.」 as the
      decimal separator, preserving sign, digits, and written
      precision. Eastern Arabic-Indic digit or Arabic-decimal-separator
      writings of the same value converge to this form.
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
      Complete dates are written as D M YYYY with one ASCII space
      between fields: ASCII digits with no leading zero for day, the
      Arabic month name of the recovered calendar (Gregorian: يناير،
      فبراير، مارس، أبريل، مايو، يونيو، يوليو، أغسطس، سبتمبر، أكتوبر،
      نوفمبر، ديسمبر; Hijri months keep their names, e.g. محرم), and a
      four-digit year. Never convert between calendars and do not infer
      an unexpressed century or missing field.
- category: numeric_expressions
  phenomenon: time
  canonical_form:
    type: generative
    instruction: >
      Clock times with expressed minutes are written in 24-hour HH:MM
      form using ASCII digits and 「:」. Resolve an expressed period-of-day
      word such as صباحاً or مساءً into the 24-hour value and omit that
      word from the canonical form. When only an hour is expressed,
      write the hour number alone without inventing minutes.
- category: numeric_expressions
  phenomenon: currency
  canonical_form:
    type: generative
    instruction: >
      Monetary amounts are written as an ASCII digit amount, one ASCII
      space, and the canonical Arabic name of the recovered currency
      identity (ريال for the Saudi riyal, دولار for the US dollar, يورو
      for the euro; add a distinguishing qualifier when the bare name is
      ambiguous, e.g. جنيه مصري vs جنيه استرليني). Symbol, abbreviation,
      and spoken-name inputs for the same currency converge to that
      name. Preserve explicitly expressed fractional precision.
- category: numeric_expressions
  phenomenon: unit
  canonical_form:
    type: generative
    instruction: >
      Measured values are written as an ASCII digit number, one ASCII
      space, and the canonical Arabic name of the recovered unit
      identity (e.g. متر، كيلومتر، سنتيمتر، كيلوجرام، غرام، لتر،
      مليلتر، درجة مئوية، درجة فهرنهايت). Symbols, abbreviations, and
      synonymous spoken unit names converge to the same unit name.
- category: numeric_expressions
  phenomenon: phone
  canonical_form:
    type: generative
    instruction: >
      Telephone numbers are written as one contiguous ASCII digit
      string with all presentation grouping separators removed.
      Preserve a leading international 「+」 when it is part of the
      recovered number. Eastern Arabic-Indic digit writings converge to
      the same ASCII digit string.
- category: numeric_expressions
  phenomenon: roman
  canonical_form:
    type: generative
    instruction: >
      A value conventionally expressed with Roman numerals is written
      in normalized uppercase Roman-numeral notation using I, V, X, L,
      C, D, M. Spelled Arabic, Arabic-digit, lowercase Roman, and
      uppercase Roman inputs with the same value converge to the same
      minimal standard Roman numeral.
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
      by the canonical Arabic marker for their recovered address role,
      such as رقم، مبنى، شقة، حي، شارع، طريق. Spoken and abbreviated
      realizations of the same role converge to that marker.
- category: symbols_markers
  phenomenon: biological
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic ar canonical rendering is
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
      Arabic written template, using the canonical structural label of
      the recovered citation type (e.g. المادة، الفقرة، الباب، الأمر
      الملكي رقم), ASCII digits, and halfwidth uppercase Latin letters
      where the citation contains them. Typographic variants converge to
      the canonical template.
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
      No sufficiently deterministic ar canonical rendering is
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
