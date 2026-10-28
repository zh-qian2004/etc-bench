# fa canonical contracts

This file declares exact `C(fa, category, phenomenon)` contracts. The ISO 639-1 filename identifies the language. Follow `../canonicalization-method.md`.

Conventions: metalanguage and schema keys are English; `category`/`phenomenon` are benchmark identifiers; canonical literals are written in Standard Persian as used in Iran exactly as the agent should output them. Each `instruction` states the canonical form of the phenomenon; it does not enumerate benchmark material or transcription-dependent cases. Category methodology never supplies a rendering fallback; without an exact applicable contract, retain the source span.

Shared rendering conventions:

```yaml
numeric_digits: ASCII 0-9; Extended Arabic-Indic digits ۰-۹ converge to ASCII
decimal_separator: "."
negative_sign: "-"
persian_script: Standard Persian, Iranian Academy (فرهنگستان) written norm
persian_codepoints: ک U+06A9 and ی U+06CC (never Arabic ك ي ى)
latin_width: halfwidth
identifier_latin_case: uppercase
phonetic_transcription:
  language: Standard Persian (Iranian norm, Tehran standard colloquial-free reading)
  representation: broad phonemic IPA
  vowel_length: marked (phonemic)
  tone: not applicable
  stress: not marked (non-phonemic)
  arabic_letter_mergers: transcribed merged (س/ص/ث → /s/, ز/ذ/ض/ظ → /z/,
    ت/ط → /t/, ه/ح → /h/, ق/غ → /ɣ/), per the fa reading norm
  connected_speech: no cross-word sandhi
  word_separator: single ASCII space
  wrapper: "/.../"
```

Canonical rendering may depend on the recovered semantic value and context inside the current record, but never on the source-side spelling, separator, symbol-versus-name choice, or another batch record.

## orthographic_variants

- category: orthographic_variants
  phenomenon: persian_arabic_codepoint_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span with Persian codepoints: ك converges to
      ک (U+06A9) and Arabic ي or ى converges to ی (U+06CC). Only the
      character encoding changes; every other letter stays as written.
- category: orthographic_variants
  phenomenon: affix_zwnj_spacing_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with ZWNJ (U+200C) between the stem and
      the productive affix: after the prefixes می and نمی, before the
      suffixes ها, تر, ترین, and between a stem and a pronominal
      enclitic when the Academy norm requires it, e.g. می‌روم,
      کتاب‌ها. Joined and space-separated writings converge to the ZWNJ
      form.
- category: orthographic_variants
  phenomenon: compound_boundary_spacing_variants
  canonical_form:
    type: generative
    instruction: >
      Render the lexicalized compound with the joining the Academy
      orthography prescribes for that item: ZWNJ for compounds the norm
      writes joined-by-ZWNJ (e.g. گفت‌وگو، جست‌وجو), plain joining for
      those prescribed solid (e.g. راهآهن), and a single space for those
      prescribed spaced. If the norm gives no joined form, retain the
      source span.
- category: orthographic_variants
  phenomenon: ezafe_after_he_variants
  canonical_form:
    type: generative
    instruction: >
      Render the ezafe after a word-final silent ه with the
      he-with-final-Hamza form هٔ, e.g. خانهٔ, نامهٔ, دربارهٔ. The ی form
      with ZWNJ and the precomposed ۀ character converge to this form.
- category: orthographic_variants
  phenomenon: arabic_hamza_spelling_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the hamza spelling of its current
      Iranian Academy dictionary entry, e.g. تأثیر, مسئول, جرئت. Variant
      spellings of the same word converge to the Academy form. If the
      Academy entry cannot be determined, retain the source span.
- category: orthographic_variants
  phenomenon: medial_y_glide_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the modern ی spelling of the
      Persian /j/ glide in āy sequences, e.g. آیین, پاییز, پایین. The
      old ئ spellings of the same word converge to the modern form.
- category: orthographic_variants
  phenomenon: merged_consonant_grapheme_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the current Iranian Academy
      dictionary spelling, e.g. طوفان, اتاق, زغال. The historical or
      non-preferred variant of the same word converges to the Academy
      form. If the Academy entry cannot be determined, retain the
      source span.
- category: orthographic_variants
  phenomenon: final_alef_maqsura_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the current Iranian Academy
      dictionary spelling for its final /ɑː/ (e.g. حتی, موسی); the
      ى-type spelling of the same word converges to the Academy form.
      For personal names, keep the registered spelling and only
      alternate between the ى and ا writings of the same name when the
      current record establishes one identity. If no reliable target is
      recoverable, retain the source span.
- category: orthographic_variants
  phenomenon: optional_diacritic_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span with all optional Persian diacritics
      (fatḥa, kasra, ḍamma, sukūn, tashdīd) and Arabic tanwīn removed,
      leaving base letters, all hamza forms, madda, and ezafe
      characters untouched, e.g. من, کتاب, لطفا. Vocalized and
      tanwīn-marked writings converge to the bare form.
## homophonic_substitutions

- category: homophonic_substitutions
  phenomenon: proper_name_adjective_homophones
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      name reading and the adjective reading of the same phonological
      word, such as شیرین, converge to /ʃiːɾiːn/. If the reading cannot
      be determined, retain the source span.
- category: homophonic_substitutions
  phenomenon: arabic_consonant_letter_mergers
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the merged Arabic-letter phonemes transcribed by their merged
      values (س/ص/ث → /s/, ز/ذ/ض/ظ → /z/, ت/ط → /t/, ه/ح → /h/, ق/غ →
      /ɣ/), e.g. ثواب and صواب converge to /sɒːb/, طوفان and توفان to
      /tufɒːn/. If the reading cannot be determined, retain the source
      span.
- category: homophonic_substitutions
  phenomenon: ayn_hamza_weakening
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the weakened or deleted ع/ء transcribed as zero, e.g. تأثیر and
      تاثیر converge to /taʔsiːr/ when both are accepted for the same
      word; when the record clearly preserves the glottal stop, transcribe
      /ʔ/. If the reading cannot be determined, retain the source span.
## numeric_expressions

- category: numeric_expressions
  phenomenon: cardinal
  canonical_form:
    type: generative
    instruction: >
      Quantities are written with ASCII digits. Spelled-out Persian
      number words, Extended Arabic-Indic digits, and ASCII digits for
      the same quantity converge to the same ASCII digit string.
- category: numeric_expressions
  phenomenon: ordinal
  canonical_form:
    type: generative
    instruction: >
      Ranks are written with ASCII digits followed by the Persian
      ordinal suffix «م» (e.g. 5م for پنجم). The spoken ordinal form of
      the same rank converges to the digit-plus-suffix form.
- category: numeric_expressions
  phenomenon: decimal
  canonical_form:
    type: generative
    instruction: >
      Decimal values are written with ASCII digits and 「.」 as the
      decimal separator, preserving sign, digits, and written
      precision. Extended Arabic-Indic digit and «٫»-separated writings
      of the same value converge to this form.
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
      Complete dates are written as D month-name YYYY with one ASCII
      space between fields: ASCII digits with no leading zero for day,
      the month name of the recovered calendar (Solar Hijri: فروردین،
      اردیبهشت، خرداد، تیر، مرداد، شهریور، مهر، آبان، آذر، دی، بهمن،
      اسفند; Gregorian: ژانویه، فوریه، مارس، آوریل، مه، ژوئن، ژوئیه،
      اوت، سپتامبر، اکتبر، نوامبر، دسامبر), and a four-digit year.
      Never convert between calendars and do not infer an unexpressed
      century or missing field.
- category: numeric_expressions
  phenomenon: time
  canonical_form:
    type: generative
    instruction: >
      Clock times with expressed minutes are written in 24-hour HH:MM
      form using ASCII digits and 「:」. Resolve an expressed period-of-day
      word such as صبح, ظهر, عصر, or شب into the 24-hour value and omit
      that word from the canonical form. When only an hour is expressed,
      write the hour number alone without inventing minutes.
- category: numeric_expressions
  phenomenon: currency
  canonical_form:
    type: generative
    instruction: >
      Monetary amounts are written as an ASCII digit amount, one ASCII
      space, and the canonical Persian name of the recovered currency
      identity (تومان or ریال for Iranian money according to the
      recovered unit, دلار for the US dollar, یورو for the euro, with a
      qualifier when the bare name is ambiguous, e.g. درهم امارات).
      Symbol, abbreviation, and spoken-name inputs for the same
      currency converge to that name. Preserve explicitly expressed
      fractional precision.
- category: numeric_expressions
  phenomenon: unit
  canonical_form:
    type: generative
    instruction: >
      Measured values are written as an ASCII digit number, one ASCII
      space, and the canonical Persian name of the recovered unit
      identity (e.g. کیلومتر، متر، سانتی‌متر، کیلوگرم، گرم، لیتر،
      میلی‌لیتر، درجه سانتی‌گراد). Symbols, abbreviations, and synonymous
      spoken unit names converge to the same unit name.
- category: numeric_expressions
  phenomenon: phone
  canonical_form:
    type: generative
    instruction: >
      Telephone numbers are written as one contiguous ASCII digit string
      with all presentation grouping separators removed. Preserve a
      leading international 「+」 when it is part of the recovered
      number. Extended Arabic-Indic digit writings converge to the same
      ASCII digit string.
- category: numeric_expressions
  phenomenon: roman
  canonical_form:
    type: generative
    instruction: >
      A value conventionally expressed with Roman numerals is written
      in normalized uppercase Roman-numeral notation using I, V, X, L,
      C, D, M. Spelled Persian, Persian-digit, lowercase Roman, and
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
      by the canonical Persian marker for their recovered address role,
      such as شماره، خیابان، کوچه، پلاک، طبقه، واحد. Spoken and
      abbreviated realizations of the same role converge to that marker.
- category: symbols_markers
  phenomenon: biological
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic fa canonical rendering is
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
      Persian written template, using the canonical structural label of
      the recovered citation type (e.g. ماده، بند، تبصره، قانون), ASCII
      digits, and halfwidth uppercase Latin letters where the citation
      contains them. Typographic variants converge to the canonical
      template.
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
      No sufficiently deterministic fa canonical rendering is
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
