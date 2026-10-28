# ru canonical contracts

This file declares exact `C(ru, category, phenomenon)` contracts. The ISO 639-1 filename identifies the language. Follow `../canonicalization-method.md`.

Conventions: metalanguage and schema keys are English; `category`/`phenomenon` are benchmark identifiers; canonical literals are written in Standard Russian exactly as the agent should output them. Each `instruction` states the canonical form of the phenomenon; it does not enumerate benchmark material or transcription-dependent cases. Category methodology never supplies a rendering fallback; without an exact applicable contract, retain the source span.

Shared rendering conventions:

```yaml
numeric_digits: ASCII 0-9
decimal_separator: "," (comma)
negative_sign: "-"
russian_orthography: Standard Russian, current academy dictionary norm
latin_width: halfwidth
identifier_latin_case: uppercase
phonetic_transcription:
  language: Standard Russian (Moscow norm)
  representation: broad phonemic IPA
  vowel_length: not marked (non-phonemic)
  stress: marked on the stressed vowel of each transcribed word
  vowel_reduction: not transcribed (orthography-neutral phonemic level)
  connected_speech: no cross-word sandhi; final devoicing and voicing
    assimilation are not transcribed at this level
  word_separator: single ASCII space
  wrapper: "/.../"
```

Canonical rendering may depend on the recovered semantic value and context inside the current record, but never on the source-side spelling, separator, symbol-versus-name choice, or another batch record.

## abbreviations

- category: abbreviations
  phenomenon: common_multiword_graphic_abbreviations
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span as the contextually recovered full Russian
      phrase with its grammatical realization, e.g. т. е. → то есть,
      и т. д. → и так далее, т. н. → так называемая before a feminine
      noun. If the expansion or its inflection is ambiguous, retain the
      source span.
- category: abbreviations
  phenomenon: single_word_dot_truncations
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span as the contextually recovered full Russian
      word with its grammatical realization, e.g. напр. → например,
      прибл. → приблизительно, вкл. → включительно. If the expansion is
      ambiguous, retain the source span.
- category: abbreviations
  phenomenon: hyphenated_suffix_contractions
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span as the recovered full word, e.g. кол-во →
      количество, кач-во → качество, изд-во → издательство. If the
      expansion is ambiguous, retain the source span.
- category: abbreviations
  phenomenon: slash_graphic_abbreviations
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span as the contextually recovered full Russian
      phrase with agreement to the governed noun, e.g. ж/д станция →
      железнодорожная станция, б/у → бывший в употреблении with its
      grammatical realization. If the expansion or agreement is
      ambiguous, retain the source span.
- category: abbreviations
  phenomenon: context_dependent_homographic_abbreviations
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span as the contextually recovered full word
      or phrase with its grammatical realization, e.g. в 2020 г. → в
      2020 году, ст. 5 закона → статья 5 закона. If the context does
      not uniquely determine the expansion, retain the source span.
- category: abbreviations
  phenomenon: doubled_plural_abbreviations
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span as the contextually recovered plural word
      with its grammatical case, e.g. гг. → годы in the recovered case,
      вв. → века, пп. → пункты. If the expansion or case is ambiguous,
      retain the source span.
## orthographic_variants

- category: orthographic_variants
  phenomenon: optional_yo_diacritic
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the letter ё where the dictionary
      form contains it, e.g. жёлтый, берёза, шёпот. The two-dot-free е
      spelling of the same word converges to the ё form.
- category: orthographic_variants
  phenomenon: lexical_vowel_doublets
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the form listed as the primary entry
      in the current academy dictionary for that lexical doublet, e.g.
      туннель, зорянка. The secondary variant of the same word converges
      to the primary form. When the dictionary lists both as fully
      equal, retain the source span.
- category: orthographic_variants
  phenomenon: optional_glide_in_anglicisms
  canonical_form:
    type: generative
    instruction: >
      Render the accepted loanword with the form listed as the primary
      entry in the current academy dictionary, e.g. плеер, флаер. The
      alternative glide spelling of the same word converges to the
      primary form.
- category: orthographic_variants
  phenomenon: iskrenne_iskrenno_adverb_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted adverb with the -е ending, e.g. искренне,
      неискренне. The -о variant of the same adverb converges to the -е
      form.
## homophonic_substitutions

- category: homophonic_substitutions
  phenomenon: given_name_common_noun_capitalization
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the stressed vowel marked, e.g. Вера and вера converge to
      /ˈvʲerə/, Роман and роман to /rɐˈman/. Capitalization is never
      transcribed. If the reading cannot be determined from the current
      record, retain the source span.
- category: homophonic_substitutions
  phenomenon: toponym_common_noun_capitalization
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the stressed vowel marked, e.g. Клин and клин converge to
      /ˈklʲin/, Бор and бор to /ˈbor/. Capitalization is never
      transcribed. If the reading cannot be determined, retain the
      source span.
- category: homophonic_substitutions
  phenomenon: yo_omission_given_names
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the /o/ reading of ё marked as stressed, e.g. Семён and Семен
      converge to /sʲɪˈmʲon/, Фёдор and Федор to /ˈfʲodər/. If the
      reading cannot be determined, retain the source span.
- category: homophonic_substitutions
  phenomenon: yo_omission_surnames
  canonical_form:
    type: generative
    instruction: >
      Render the accepted surname's contextually determined
      pronunciation in broad phonemic IPA under the shared phonetic
      conventions, with the /o/ reading of ё marked as stressed, e.g.
      Семёнов and Семенов converge to /sʲɪˈmʲonəf/, Королёв and Королев
      to /kərɐˈlʲof/. If the reading cannot be determined, retain the
      source span.
- category: homophonic_substitutions
  phenomenon: yo_omission_pronouns
  canonical_form:
    type: generative
    instruction: >
      Render the accepted pronoun's contextually determined
      pronunciation in broad phonemic IPA under the shared phonetic
      conventions, with the /o/ reading of ё marked as stressed, e.g.
      её and ее converge to /jɪˈjo/, неё and нее to /nʲɪˈjo/.
- category: homophonic_substitutions
  phenomenon: homophonous_female_name_spelling_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, e.g.
      Майя and Мая converge to /ˈmajə/, Тайя and Тая to /ˈtajə/, Кайя
      and Кая to /ˈkajə/. If the reading cannot be determined, retain
      the source span.
- category: homophonic_substitutions
  phenomenon: geminate_neutralization_in_names
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the geminate not transcribed as length, e.g. Жанна and Жана →
      /ˈʐanə/, Инна and Ина → /ˈinə/, Эмма and Эма → /ˈɛmə/. If the
      reading cannot be determined, retain the source span.
## numeric_expressions

- category: numeric_expressions
  phenomenon: cardinal
  canonical_form:
    type: generative
    instruction: >
      Quantities are written with ASCII digits. Spelled-out Russian
      number words and digits for the same quantity converge to the
      same ASCII digit string.
- category: numeric_expressions
  phenomenon: ordinal
  canonical_form:
    type: generative
    instruction: >
      Ranks are written with ASCII digits followed by a period (the
      Russian ordinal point), e.g. 5. for пятый. Spelled ordinal words
      converge to the digit-plus-period form.
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
      form using ASCII digits and 「:」. Resolve an expressed period-of-day
      word such as утра, дня, вечера, or ночи into the 24-hour value and
      omit that word from the canonical form. When only an hour is
      expressed, write the hour number alone without inventing minutes.
- category: numeric_expressions
  phenomenon: currency
  canonical_form:
    type: generative
    instruction: >
      Monetary amounts are written as an ASCII digit amount, one ASCII
      space, and the canonical Russian name of the recovered currency
      identity in the grammatical case required by the amount (рублей,
      доллара, евро, фунта стерлингов, with a qualifier when the bare
      name is ambiguous, e.g. канадского доллара). Symbol, abbreviation,
      and spoken-name inputs for the same currency converge to that
      name. Preserve explicitly expressed fractional precision.
- category: numeric_expressions
  phenomenon: unit
  canonical_form:
    type: generative
    instruction: >
      Measured values are written as an ASCII digit number, one ASCII
      space, and the canonical Russian name of the recovered unit
      identity (e.g. километров, метров, сантиметров, килограммов,
      граммов, литров, миллилитров, градусов Цельсия, часов). Symbols,
      abbreviations (км, кг), and synonymous spoken unit names converge
      to the same unit name.
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
      C, D, M. Spelled Russian, lowercase Roman, and uppercase Roman
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
      by the canonical Russian marker for their recovered address role,
      such as улица, дом, корпус, строение, квартира, этаж, офис.
      Spoken and abbreviated realizations of the same role converge to
      that marker.
- category: symbols_markers
  phenomenon: biological
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic ru canonical rendering is
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
      Russian direction phrases and the с. ш./ю. ш./в. д./з. д.
      convention converge to the same uppercase-letter notation.
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
      Russian written template, using the canonical structural label of
      the recovered citation type (e.g. статья, пункт, часть, УК РФ),
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
      No sufficiently deterministic ru canonical rendering is
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
