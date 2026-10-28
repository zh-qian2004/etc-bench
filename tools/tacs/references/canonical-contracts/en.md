# en canonical contracts

This file declares exact `C(en, category, phenomenon)` contracts. The ISO 639-1 filename identifies the language. Follow `../canonicalization-method.md`.

Conventions: metalanguage and schema keys are English; `category`/`phenomenon` are benchmark identifiers; canonical literals are written in American English exactly as the agent should output them. Each `instruction` states the canonical form of the phenomenon; it does not enumerate benchmark material or transcription-dependent cases. Category methodology never supplies a rendering fallback; without an exact applicable contract, retain the source span.

Shared rendering conventions:

```yaml
numeric_digits: ASCII 0-9
decimal_separator: "."
negative_sign: "-"
english_spelling: American English (Merriam-Webster / US convention)
latin_width: halfwidth
identifier_latin_case: uppercase
phonetic_transcription:
  language: General American English
  representation: broad phonemic IPA
  rhoticity: transcribed /r/ (rhotic)
  vowel_length: not marked (quality+stress carry contrast)
  stress: marked on the primary-stressed syllable
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
      American English expansion, e.g. Dr. → Doctor, St. → Street,
      e.g. → for example. Apply the grammatical realization required
      by the surrounding syntax. If the expansion is ambiguous, retain
      the source span.
## orthographic_variants

- category: orthographic_variants
  phenomenon: british_american_spelling
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word in its American spelling, e.g. color,
      center, theater, realize, catalog. The British spelling of the
      same word converges to the American form.
- category: orthographic_variants
  phenomenon: hyphen_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the current Merriam-Webster primary
      spelling's hyphenation, e.g. email, cooperate. The alternative
      hyphenated spelling of the same word converges to the primary
      form. When the dictionary lists both forms as equal variants,
      retain the source span.
- category: orthographic_variants
  phenomenon: diacritic_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted loanword with the diacritics of its
      Merriam-Webster primary entry, e.g. café, naïve, résumé. The
      diacritic-free spelling of the same word converges to the primary
      form. When the primary entry itself is diacritic-free, remove
      the diacritics.
- category: orthographic_variants
  phenomenon: inflectional_consonant_doubling
  canonical_form:
    type: generative
    instruction: >
      Render the accepted inflected form with the single consonant
      preferred by the American convention, e.g. traveled, canceled,
      labeled, modeling. The doubled-consonant variant of the same form
      converges to the single-consonant form.
## homophonic_substitutions

- category: homophonic_substitutions
  phenomenon: homophonic_names
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad IPA under the shared phonetic conventions, with primary
      stress marked and full /r/, e.g. John and Jon → /dʒɑn/, Sara and
      Sarah → /ˈsɛrə/, Allen and Alan → /ˈælən/. If the reading cannot
      be determined from the current record, retain the source span.
- category: homophonic_substitutions
  phenomenon: common_homophones
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word's contextually determined pronunciation
      in broad IPA under the shared phonetic conventions, with primary
      stress marked, e.g. to, too, and two → /tu/, right and write →
      /raɪt/, flower and flour → /ˈflaʊɚ/. If the reading cannot be
      determined, retain the source span.
## numeric_expressions

- category: numeric_expressions
  phenomenon: cardinal
  canonical_form:
    type: generative
    instruction: >
      Quantities are written with ASCII digits. Spelled-out English
      number words and digits for the same quantity converge to the
      same ASCII digit string.
- category: numeric_expressions
  phenomenon: ordinal
  canonical_form:
    type: generative
    instruction: >
      Ranks are written with ASCII digits followed by the lowercase
      suffixes st, nd, rd, th without a hyphen, e.g. 21st, 2nd, 3rd,
      47th. Spelled ordinal words converge to the digit-plus-suffix
      form.
- category: numeric_expressions
  phenomenon: decimal
  canonical_form:
    type: generative
    instruction: >
      Decimal values are written with ASCII digits and 「.」 as the
      decimal separator, preserving sign, digits, and written
      precision.
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
      Complete dates are written in month-day-year order: MMMM D, YYYY
      with the American English month name, the day with no leading
      zero, an ASCII comma, one ASCII space, and the four-digit year,
      e.g. July 3, 2026. Numeric writings of the same date converge to
      this form. Do not infer an unexpressed century or missing field.
- category: numeric_expressions
  phenomenon: time
  canonical_form:
    type: generative
    instruction: >
      Clock times with expressed minutes are written in 12-hour H:MM
      form using ASCII digits and 「:」, followed by one ASCII space and
      lowercase am or pm, e.g. 9:45 am. Resolve a spoken quarter/half
      expression or period-of-day word into the 12-hour value and the
      correct marker. When only an hour is expressed, write the hour
      with its am/pm marker without inventing minutes.
- category: numeric_expressions
  phenomenon: currency
  canonical_form:
    type: generative
    instruction: >
      Monetary amounts are written as the canonical American English
      currency name followed by the ASCII digit amount, e.g. 12
      dollars, 5 dollars 50 cents for a expressed compound amount. The
      symbol form ($12), spoken name, and abbreviation of the same
      amount converge to the name-plus-digits form; other currencies
      use their canonical English names (euros, yen, pounds sterling).
      Preserve explicitly expressed fractional precision.
- category: numeric_expressions
  phenomenon: unit
  canonical_form:
    type: generative
    instruction: >
      Measured values are written as an ASCII digit number, one ASCII
      space, and the canonical American English name of the recovered
      unit identity (e.g. kilometers, meters, centimeters, kilograms,
      grams, liters, milliliters, degrees Celsius). Symbols,
      abbreviations (km, kg), and synonymous spoken unit names converge
      to the same unit name.
- category: numeric_expressions
  phenomenon: phone
  canonical_form:
    type: generative
    instruction: >
      Telephone numbers are written as one contiguous ASCII digit
      string with all presentation grouping separators removed.
      Preserve a leading international 「+」 when it is part of the
      recovered number.
- category: numeric_expressions
  phenomenon: roman
  canonical_form:
    type: generative
    instruction: >
      A value conventionally expressed with Roman numerals is written
      in normalized uppercase Roman-numeral notation using I, V, X, L,
      C, D, M. Spelled English, lowercase Roman, and uppercase Roman
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
      by the canonical American English marker for their recovered
      address role, such as Street, Avenue, Boulevard, Road, Suite,
      Apartment, Floor, P.O. Box. Spoken and abbreviated realizations
      of the same role converge to that marker.
- category: symbols_markers
  phenomenon: biological
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic en canonical rendering is
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
      fields. Direction is written as uppercase N, S, E, or W. Decimal
      degrees keep their point. Spoken and symbolic inputs with the
      same coordinate value converge to this notation.
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
      American English written template, using the canonical
      structural label of the recovered citation type (e.g. Section,
      Article, U.S.C.), ASCII digits, and halfwidth uppercase Latin
      letters where the citation contains them. Typographic variants
      converge to the canonical template.
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
      No sufficiently deterministic en canonical rendering is
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
