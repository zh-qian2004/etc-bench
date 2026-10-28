# de canonical contracts

This file declares exact `C(de, category, phenomenon)` contracts. The ISO 639-1 filename identifies the language. Follow `../canonicalization-method.md`.

Conventions: metalanguage and schema keys are English; `category`/`phenomenon` are benchmark identifiers; canonical literals are written in Standard German of Germany (Hochdeutsch) exactly as the agent should output them. Each `instruction` states the canonical form of the phenomenon; it does not enumerate benchmark material or transcription-dependent cases. Category methodology never supplies a rendering fallback; without an exact applicable contract, retain the source span.

Shared rendering conventions:

```yaml
numeric_digits: ASCII 0-9
decimal_separator: ","
negative_sign: "-"
german_orthography: Standard German (Germany), current official orthography
latin_width: halfwidth
identifier_latin_case: uppercase
phonetic_transcription:
  language: Standard German (Germany)
  representation: broad phonemic IPA
  vowel_length: marked (phonemic)
  stress: marked on the primary-stressed syllable
  final_devoicing: not transcribed (orthography neutral)
  connected_speech: no cross-word sandhi
  word_separator: single ASCII space
  wrapper: "/.../"
```

Canonical rendering may depend on the recovered semantic value and context inside the current record, but never on the source-side spelling, separator, symbol-versus-name choice, or another batch record.

## abbreviations

- category: abbreviations
  phenomenon: abbreviation
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span as the contextually recovered full
      German phrase, e.g. z.B. → zum Beispiel, usw. → und so weiter,
      bzw. → beziehungsweise. Apply the grammatical realization
      required by the surrounding syntax. If the expansion is ambiguous,
      retain the source span.
## orthographic_variants

- category: orthographic_variants
  phenomenon: eszett_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with ß for the /s/ after a long vowel or
      diphthong, e.g. Straße, Fuß, Spaß; the ss spelling of the same
      word converges to the ß spelling. Where the current official
      orthography itself requires ss (after short vowels, or in
      all-caps contexts rendered in lowercase), keep ss.
- category: orthographic_variants
  phenomenon: umlaut_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the umlaut letters ä, ö, ü; the
      substitute spellings ae, oe, ue of the same word converge to the
      umlaut spelling, e.g. Müller, schön, für.
- category: orthographic_variants
  phenomenon: foreign_word_spelling
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the Duden-recommended spelling of
      the recovered loanword, e.g. Joghurt, Fantasie, Delfin, Grafik,
      Telefon. The alternative dictionary-recognized spelling of the
      same word converges to the recommended one.
- category: orthographic_variants
  phenomenon: native_lexical_variant_spellings
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the Duden-preferred variant of the
      recovered lexical doublet, e.g. aufwändig, Quäntchen; the other
      dictionary-recognized spelling converges to the preferred one.
      When Duden lists both variants without preference, retain the
      source span.
- category: orthographic_variants
  phenomenon: compound_spacing_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted compound in the spacing required by the
      current official orthography for the recovered word class and
      syntactic environment: written-together for deverbal compounds and
      fixed connectors that current rules prescribe as one word (e.g.
      kennenlernen, sodass), and the form the rules prescribe for Rad
      fahren. Only apply where current rules uniquely determine one
      spacing; otherwise retain the source span.
## homophonic_substitutions

- category: homophonic_substitutions
  phenomenon: homophonic_names
  canonical_form:
    type: generative
    instruction: >
      Render the accepted surname's contextually determined
      pronunciation in broad IPA under the shared phonetic conventions,
      with primary stress marked, e.g. Meyer, Maier, Meier, Mayer →
      /ˈmaɪ̯ɐ/, Schmidt, Schmitt, Schmid → /ʃmɪt/. If the reading
      cannot be determined from the current record, retain the source
      span.
- category: homophonic_substitutions
  phenomenon: homophones
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word's contextually determined pronunciation
      in broad IPA under the shared phonetic conventions, with primary
      stress marked, e.g. das and dass → /das/, Waise and Weise →
      /ˈvaɪ̯zə/. If the reading cannot be determined, retain the source
      span.
## numeric_expressions

- category: numeric_expressions
  phenomenon: cardinal
  canonical_form:
    type: generative
    instruction: >
      Quantities are written with ASCII digits. Spelled-out German
      number words and digits for the same quantity converge to the
      same ASCII digit string.
- category: numeric_expressions
  phenomenon: ordinal
  canonical_form:
    type: generative
    instruction: >
      Ranks are written with ASCII digits followed by a period (the
      German ordinal point), e.g. 5. for fünfter. Spelled ordinal words
      converge to the digit-plus-period form.
- category: numeric_expressions
  phenomenon: decimal
  canonical_form:
    type: generative
    instruction: >
      Decimal values are written with ASCII digits and 「,」 (comma) as
      the decimal separator, preserving sign, digits, and written
      precision. Point-separated writings of the same value converge to
      the comma form.
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
      Complete dates are written in numeric day-month-year order:
      DD.MM.YYYY with ASCII digits, a two-digit day, two-digit month,
      and four-digit year, e.g. 03.07.2026. Spelled-out dates converge
      to this numeric form. Do not infer an unexpressed century or
      missing field.
- category: numeric_expressions
  phenomenon: time
  canonical_form:
    type: generative
    instruction: >
      Clock times with expressed minutes are written in 24-hour HH:MM
      form using ASCII digits and 「:」, e.g. 09:45 for Viertel vor
      zehn or 15:30 for halb vier nachmittags. Resolve an expressed
      period-of-day word into the 24-hour value and omit that word from
      the canonical form. When only an hour is expressed, write the
      hour number alone without inventing minutes.
- category: numeric_expressions
  phenomenon: currency
  canonical_form:
    type: generative
    instruction: >
      Monetary amounts are written as an ASCII digit amount, one ASCII
      space, and the canonical German name of the recovered currency
      identity (Euro, US-Dollar, Pfund, Schweizer Franken, with a
      qualifier when the bare name is ambiguous, e.g. kanadischer
      Dollar). Symbol, abbreviation, and spoken-name inputs for the
      same currency converge to that name. Preserve explicitly
      expressed fractional precision.
- category: numeric_expressions
  phenomenon: unit
  canonical_form:
    type: generative
    instruction: >
      Measured values are written as an ASCII digit number, one ASCII
      space, and the canonical German name of the recovered unit
      identity (e.g. Kilometer, Meter, Zentimeter, Kilogramm, Gramm,
      Liter, Milliliter, Grad Celsius, Stunden). Symbols, abbreviations
      (e.g. km, kg), and synonymous spoken unit names converge to the
      same unit name.
- category: numeric_expressions
  phenomenon: phone
  canonical_form:
    type: generative
    instruction: >
      Telephone numbers are written as one contiguous ASCII digit
      string with all presentation grouping separators removed.
      Preserve a leading international 「+」 and any expressed digit
      groups in their recovered order.
- category: numeric_expressions
  phenomenon: roman
  canonical_form:
    type: generative
    instruction: >
      A value conventionally expressed with Roman numerals is written
      in normalized uppercase Roman-numeral notation using I, V, X, L,
      C, D, M. Spelled German, lowercase Roman, and uppercase Roman
      inputs with the same value converge to the same minimal standard
      Roman numeral.
- category: numeric_expressions
  phenomenon: sports_score
  canonical_form:
    type: generative
    instruction: >
      A competition score is written as two ASCII digit numbers joined
      by the ASCII colon 「:」 in competitor order, independent of the
      source separator.
## symbols_markers

- category: symbols_markers
  phenomenon: address
  canonical_form:
    type: generative
    instruction: >
      Numeric address components are written with ASCII digits followed
      by the canonical German marker for their recovered address role,
      such as Straße, Platz, Hausnummer, Wohnung, Etage, Postfach.
      Spoken and abbreviated realizations of the same role converge to
      that marker.
- category: symbols_markers
  phenomenon: biological
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic de canonical rendering is
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
      fields. Direction is written as uppercase N, S, O (Ost), or W.
      Spoken and symbolic inputs with the same coordinate value
      converge to this notation.
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
      German written template, using the canonical structural label of
      the recovered citation type (e.g. Art., Abs., Satz, GG), ASCII
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
      No sufficiently deterministic de canonical rendering is
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
