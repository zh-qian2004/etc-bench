# fr canonical contracts

This file declares exact `C(fr, category, phenomenon)` contracts. The ISO 639-1 filename identifies the language. Follow `../canonicalization-method.md`.

Conventions: metalanguage and schema keys are English; `category`/`phenomenon` are benchmark identifiers; canonical literals are written in Standard French (France) exactly as the agent should output them. Each `instruction` states the canonical form of the phenomenon; it does not enumerate benchmark material or transcription-dependent cases. Category methodology never supplies a rendering fallback; without an exact applicable contract, retain the source span.

Shared rendering conventions:

```yaml
numeric_digits: ASCII 0-9
decimal_separator: ","
negative_sign: "-"
french_orthography: Standard French (France), Larousse/Robert dictionary norm
reform_policy: 1990 rectifications accepted; dictionary primary form is canonical
latin_width: halfwidth
identifier_latin_case: uppercase
phonetic_transcription:
  language: Standard French (France)
  representation: broad phonemic IPA
  vowel_length: not marked (non-phonemic)
  stress: not marked (fixed phrase-final, non-phonemic)
  final_consonants: orthographic consonants not pronounced in the standard
    reading are not transcribed
  connected_speech: liaison applied only where the standard reading
    requires it; no other cross-word sandhi
  word_separator: single ASCII space
  wrapper: "/.../"
```

Canonical rendering may depend on the recovered semantic value and context inside the current record, but never on the source-side spelling, separator, symbol-versus-name choice, or another batch record.

## abbreviations

- category: abbreviations
  phenomenon: fixed_phrase_abbreviations
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span as the contextually recovered full French
      phrase, e.g. etc. → et cetera, c.-à-d. → c'est-à-dire, p. ex. →
      par exemple. Apply the grammatical realization required by the
      surrounding syntax. If the expansion is ambiguous, retain the
      source span.
## orthographic_variants

- category: orthographic_variants
  phenomenon: circumflex_i_u_reform
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the circumflex removed where the
      1990 rectifications allow omission on i and u, e.g. cout,
      paraitre, entrainer. The traditional circumflexed spelling of the
      same word converges to the rectified form. Keep the circumflex
      where the rectifications or usage require it (dû, mûr, sûr, jeûne,
      passé simple and imperfect subjunctive endings).
- category: orthographic_variants
  phenomenon: grave_accent_harmonization
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the grave accent è before a
      syllable containing a mute e, per the 1990 rectification, e.g.
      évènement, règlementaire, je cèderai. The traditional
      acute-accent spelling of the same word converges to the grave
      form.
- category: orthographic_variants
  phenomenon: eler_eter_consonant_reform
  canonical_form:
    type: generative
    instruction: >
      Render the conjugated form of the -eler/-eter verb with è plus a
      single consonant per the 1990 rectification, e.g. j'amoncèle, tu
      époussètes, il ruissèle. The traditional doubled-consonant form of
      the same form converges to the rectified form. Keep the doubled
      consonant for appeler, jeter, and their derivatives, which the
      rectifications leave unchanged.
- category: orthographic_variants
  phenomenon: diaeresis_repositioning
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the diaeresis on the vowel that is
      actually pronounced separately, per the 1990 rectification, e.g.
      aigüe, ambigüe, gageüre, argüer. The traditional placement of the
      same word converges to the rectified form.
- category: orthographic_variants
  phenomenon: compound_solidification
  canonical_form:
    type: generative
    instruction: >
      Render the accepted compound as one solid word per the 1990
      rectification where the dictionary recognizes the solid form,
      e.g. weekend, portemonnaie, tictac. The hyphenated spelling of the
      same compound converges to the solid form.
- category: orthographic_variants
  phenomenon: compound_plural_regularization
  canonical_form:
    type: generative
    instruction: >
      Render the accepted compound noun plural with the regularized
      marking per the 1990 rectification, e.g. des après-midis, des
      pèse-lettres, un compte-goutte. The traditional plural of the
      same compound converges to the rectified form. Keep the
      grammatical number recovered from the record.
- category: orthographic_variants
  phenomenon: loanword_plural_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted loanword plural with the French regular -s
      plural, e.g. matchs, maximums, sandwichs. The foreign or learned
      plural of the same word converges to the French form.
- category: orthographic_variants
  phenomenon: loanword_diacritic_adaptation
  canonical_form:
    type: generative
    instruction: >
      Render the accepted loanword with the diacritics of its primary
      Larousse/Robert dictionary entry, e.g. diésel, révolver, allégro.
      The undiacritized spelling of the same word converges to the
      dictionary-primary form. When the primary entry itself carries no
      diacritic, remove the added diacritic.
- category: orthographic_variants
  phenomenon: hyphenated_number_reform
  canonical_form:
    type: generative
    instruction: >
      Render the accepted compound numeral with hyphens between all its
      component words per the 1990 rectification, e.g. vingt-et-un,
      cent-trois, deux-mille-cinq-cents. The traditionally spaced
      spelling of the same numeral converges to the fully hyphenated
      form. Treat million and milliard as nouns joined with single
      spaces, e.g. deux millions.
- category: orthographic_variants
  phenomenon: ayer_i_y_conjugation_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted conjugated form of the -ayer verb with the i
      stem where the verb's standard conjugation table allows both,
      e.g. je paie, j'essaie, il balaie, je paierai. The y-stem form of
      the same verb form converges to the i-stem form. For verbs whose
      tables allow only one stem, keep that stem.
- category: orthographic_variants
  phenomenon: established_lexical_doublets
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the form listed as the primary
      entry in the Larousse/Robert dictionary for that lexical doublet,
      e.g. clé, cuillère, lis. The secondary variant of the same word
      converges to the primary form. When the dictionary lists both as
      fully equal with no primary, retain the source span.
## homophonic_substitutions

- category: homophonic_substitutions
  phenomenon: proper_name_common_word_homophones
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad IPA under the shared phonetic conventions, e.g. the name
      Jean and the noun gens converge to /ʒɑ̃/, Claire and clair to
      /klɛʁ/, Maud and mot to /mo/. Capitalization is never
      transcribed. If the reading cannot be determined from the current
      record, retain the source span.
- category: homophonic_substitutions
  phenomenon: proper_name_proper_name_homophones
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad IPA under the shared phonetic conventions. Distinct
      proper names with identical standard pronunciation converge, e.g.
      Renaud and Renault → /ʁəno/, Anne and Ann → /an/. If the reading
      cannot be determined, retain the source span.
- category: homophonic_substitutions
  phenomenon: proper_name_graphemic_spelling_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad IPA under the shared phonetic conventions. Graphemic
      variants that share one standard pronunciation converge, e.g.
      Catherine and Katherine → /katʁin/, Sofia and Sophia → /sɔfja/,
      Kevin and Kévin → /kevɛ̃/. If the reading cannot be determined,
      retain the source span.
- category: homophonic_substitutions
  phenomenon: diacritic_omission_homophones
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad IPA under the shared phonetic conventions. The
      diacritized and bare spellings of the same phonological word
      converge, e.g. Éric and Eric → /eʁik/, où and ou → /u/, là and la
      → /la/. If the reading cannot be determined, retain the source
      span.
## numeric_expressions

- category: numeric_expressions
  phenomenon: cardinal
  canonical_form:
    type: generative
    instruction: >
      Quantities are written with ASCII digits. Spelled-out French
      number words and digits for the same quantity converge to the
      same ASCII digit string.
- category: numeric_expressions
  phenomenon: ordinal
  canonical_form:
    type: generative
    instruction: >
      Ranks are written with ASCII digits followed by a superscript
      ordinal suffix: 1er / 1re, 2e, 3e, 21e (only 1 takes er/re; all
      other ranks take e). Spelled ordinal words converge to the
      digit-plus-suffix form.
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
      DD/MM/YYYY with ASCII digits, a two-digit day, two-digit month,
      and four-digit year, e.g. 03/07/2026. Spelled-out dates converge
      to this numeric form. Do not infer an unexpressed century or
      missing field.
- category: numeric_expressions
  phenomenon: time
  canonical_form:
    type: generative
    instruction: >
      Clock times with expressed minutes are written in 24-hour HH:MM
      form using ASCII digits and 「:」, e.g. 09h45 is written 09:45.
      Resolve an expressed period-of-day word such as du matin or du
      soir into the 24-hour value and omit that word from the canonical
      form. When only an hour is expressed, write the hour number alone
      without inventing minutes.
- category: numeric_expressions
  phenomenon: currency
  canonical_form:
    type: generative
    instruction: >
      Monetary amounts are written as an ASCII digit amount, one ASCII
      space, and the canonical French name of the recovered currency
      identity (euros, dollars, livres sterling, francs suisses, with a
      qualifier when the bare name is ambiguous, e.g. dollars
      canadiens). Symbol, abbreviation, and spoken-name inputs for the
      same currency converge to that name. Preserve explicitly
      expressed fractional precision.
- category: numeric_expressions
  phenomenon: unit
  canonical_form:
    type: generative
    instruction: >
      Measured values are written as an ASCII digit number, one ASCII
      space, and the canonical French name of the recovered unit
      identity (e.g. kilomètres, mètres, centimètres, kilogrammes,
      grammes, litres, millilitres, degrés Celsius, heures). Symbols,
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
      C, D, M. Spelled French, lowercase Roman, and uppercase Roman
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
      by the canonical French marker for their recovered address role,
      such as rue, avenue, boulevard, place, appartement, étage, boîte
      postale. Spoken and abbreviated realizations of the same role
      converge to that marker.
- category: symbols_markers
  phenomenon: biological
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic fr canonical rendering is
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
      fields. Direction is written as uppercase N, S, E, or O. Spoken
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
      French written template, using the canonical structural label of
      the recovered citation type (e.g. article, alinéa, Code civil),
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
      No sufficiently deterministic fr canonical rendering is
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
