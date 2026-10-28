# hi canonical contracts

This file declares exact `C(hi, category, phenomenon)` contracts. The ISO 639-1 filename identifies the language. Follow `../canonicalization-method.md`.

Conventions: metalanguage and schema keys are English; `category`/`phenomenon` are benchmark identifiers; canonical literals are written in Standard Hindi (Modern Standard Hindi, Devanagari script) exactly as the agent should output them. Each `instruction` states the canonical form of the phenomenon; it does not enumerate benchmark material or transcription-dependent cases. Category methodology never supplies a rendering fallback; without an exact applicable contract, retain the source span.

Shared rendering conventions:

```yaml
numeric_digits: ASCII 0-9; Devanagari digits converge to ASCII digits
decimal_separator: "."
negative_sign: "-"
hindi_script: Modern Standard Hindi, Devanagari script
latin_width: halfwidth
identifier_latin_case: uppercase
phonetic_transcription:
  language: Modern Standard Hindi (educated Indian reading norm)
  representation: broad phonemic IPA
  vowel_length: marked (phonemic)
  tone: not applicable
  stress: not marked (non-phonemic)
  nukta_contrasts: transcribed according to the phenomenon's stated
    merger (e.g. ज़/ज → /dʒ/, क़/क → /k/) only when the phenomenon
    declares the merger
  connected_speech: no cross-word sandhi; schwa deletion follows the
    standard reading
  word_separator: single ASCII space
  wrapper: "/.../"
```

Canonical rendering may depend on the recovered semantic value and context inside the current record, but never on the source-side spelling, separator, symbol-versus-name choice, or another batch record.

## orthographic_variants

- category: orthographic_variants
  phenomenon: q_nukta_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the nukta form क़ for the
      Perso-Arabic /q/ sound; the nukta-free क spelling of the same
      loanword converges to the nukta form, e.g. क़िला, क़ीमत, क़ायदा.
- category: orthographic_variants
  phenomenon: kh_nukta_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the nukta form ख़ for the
      Perso-Arabic /x/ sound; the nukta-free ख spelling of the same
      loanword converges to the nukta form, e.g. ख़बर, ख़त्म, ख़ास.
- category: orthographic_variants
  phenomenon: gh_nukta_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the nukta form ग़ for the
      Perso-Arabic /ɣ/ sound; the nukta-free ग spelling of the same
      loanword converges to the nukta form, e.g. ग़रीब, ग़लत, ग़ायब.
- category: orthographic_variants
  phenomenon: z_nukta_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the nukta form ज़ for the /z/ sound;
      the nukta-free ज spelling of the same loanword converges to the
      nukta form, e.g. ज़रूरी, ज़िंदगी, ज़मीन.
- category: orthographic_variants
  phenomenon: f_nukta_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the nukta form फ़ for the /f/ sound;
      the nukta-free फ spelling of the same loanword converges to the
      nukta form, e.g. फ़ायदा, फ़र्क, फ़िल्म.
- category: orthographic_variants
  phenomenon: chandrabindu_anusvara_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the chandrabindu ँ for vowel
      nasalization; the anusvara ं spelling of the same nasalized vowel
      converges to the chandrabindu form, e.g. माँ, हँसना, गाँव.
- category: orthographic_variants
  phenomenon: anusvara_homorganic_nasal_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with anusvara ं for a nasal before a
      consonant; the explicit homorganic nasal-consonant spelling of the
      same word converges to the anusvara form, e.g. हिंदी, संपत्ति,
      अंतर.
- category: orthographic_variants
  phenomenon: iye_ie_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted verb form with the short ending -िए (no
      inserted य); the -िये spelling of the same form converges to the
      short form, e.g. किए, लिए, दिए.
- category: orthographic_variants
  phenomenon: yi_i_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted form with the plain vowel ending -ई (no
      inserted य); the -यी spelling of the same form converges to the
      plain form, e.g. नई, गई, आई.
- category: orthographic_variants
  phenomenon: visarga_retention_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word without the visarga; the visarga-bearing
      tatsama spelling of the same word converges to the modern
      visarga-free form, e.g. दुख, निशब्द, निस्वार्थ.
- category: orthographic_variants
  phenomenon: foreign_rounded_vowel_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted loanword with the candra-o vowel sign ऑ; the
      आ or ओ spellings of the same loanword converge to the ऑ form,
      e.g. कॉलेज, ऑफिस, डॉक्टर.
## homophonic_substitutions

- category: homophonic_substitutions
  phenomenon: z_j_name_merger
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the merged reading /dʒ/ for ज़ and ज, e.g. ज़ाकिर and जाकिर
      converge to /dʒaːkir/. If the reading cannot be determined from
      the current record, retain the source span.
- category: homophonic_substitutions
  phenomenon: f_ph_name_merger
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the merged reading /pʰ/ for फ़ and फ, e.g. फ़रहान and फरहान converge
      to /pʰʌrɦaːn/. If the reading cannot be determined, retain the
      source span.
- category: homophonic_substitutions
  phenomenon: kh_kh_nukta_name_merger
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the merged reading /kʰ/ for ख़ and ख, e.g. ख़ान and खान converge to
      /kʰaːn/. If the reading cannot be determined, retain the source
      span.
- category: homophonic_substitutions
  phenomenon: q_k_name_merger
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the merged reading /k/ for क़ and क, e.g. क़ासिम and कासिम converge
      to /kaːsim/. If the reading cannot be determined, retain the source
      span.
- category: homophonic_substitutions
  phenomenon: gh_g_name_merger
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the merged reading /ɡ/ for ग़ and ग, e.g. ग़ालिब and गालिब converge
      to /ɡaːlib/. If the reading cannot be determined, retain the
      source span.
- category: homophonic_substitutions
  phenomenon: colloquial_demonstrative_pronoun_spelling
  canonical_form:
    type: generative
    instruction: >
      Render the accepted pronoun's contextually determined colloquial
      pronunciation in broad phonemic IPA under the shared phonetic
      conventions: वह and वो converge to /ʋoː/, यह and ये to /jeː/, वे to
      /ʋeː/ only when the record shows the colloquial merged reading. If
      the record clearly expresses a careful reading that distinguishes
      वह /ʋəɦ/ from वो, transcribe that distinction instead. If the
      reading cannot be determined, retain the source span.
## numeric_expressions

- category: numeric_expressions
  phenomenon: cardinal
  canonical_form:
    type: generative
    instruction: >
      Quantities are written with ASCII digits. Spelled-out Hindi
      number words, Devanagari digits, and ASCII digits for the same
      quantity converge to the same ASCII digit string.
- category: numeric_expressions
  phenomenon: ordinal
  canonical_form:
    type: generative
    instruction: >
      Ranks are written with ASCII digits; the Hindi ordinal form of the
      same rank converges to the bare digit string of the rank value.
- category: numeric_expressions
  phenomenon: decimal
  canonical_form:
    type: generative
    instruction: >
      Decimal values are written with ASCII digits and 「.」 as the
      decimal separator, preserving sign, digits, and written
      precision. Devanagari-digit writings of the same value converge
      to this form.
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
      Complete dates are written as D माह YYYY with one ASCII space
      between fields: ASCII digits with no leading zero for day, the
      Hindi month name of the recovered calendar (Gregorian: जनवरी,
      फ़रवरी, मार्च, अप्रैल, मई, जून, जुलाई, अगस्त, सितंबर, अक्टूबर, नवंबर,
      दिसंबर), and a four-digit year. Do not infer an unexpressed
      century or missing field.
- category: numeric_expressions
  phenomenon: time
  canonical_form:
    type: generative
    instruction: >
      Clock times with expressed minutes are written in 12-hour H:MM
      form using ASCII digits and 「:」, followed by one ASCII space and
      the Hindi period marker पूर्वाह्न (before noon) or अपराह्न (after
      noon). Resolve a spoken period-of-day word such as सुबह, दोपहर,
      शाम, or रात into the 12-hour value and the corresponding marker.
      When only an hour is expressed, write the hour number alone
      without inventing minutes.
- category: numeric_expressions
  phenomenon: currency
  canonical_form:
    type: generative
    instruction: >
      Monetary amounts are written as an ASCII digit amount followed by
      the canonical Hindi name of the recovered currency identity
      (रुपये for the Indian rupee, डॉलर for the US dollar, यूरो for the
      euro, पाउंड for the pound sterling, with a qualifier when the bare
      name is ambiguous, e.g. सऊदी रियाल). Symbol, abbreviation, and
      spoken-name inputs for the same currency converge to that name.
      Preserve explicitly expressed fractional precision, e.g. 5 रुपये
      50 पैसे for an expressed compound amount.
- category: numeric_expressions
  phenomenon: unit
  canonical_form:
    type: generative
    instruction: >
      Measured values are written as an ASCII digit number, one ASCII
      space, and the canonical Hindi name of the recovered unit
      identity (e.g. किलोमीटर, मीटर, सेंटीमीटर, किलोग्राम, ग्राम, लीटर,
      मिलीलीटर, डिग्री सेल्सियस, घंटे). Symbols, abbreviations, and
      synonymous spoken unit names converge to the same unit name.
- category: numeric_expressions
  phenomenon: phone
  canonical_form:
    type: generative
    instruction: >
      Telephone numbers are written as one contiguous ASCII digit string
      with all presentation grouping separators removed. Preserve a
      leading international 「+」 when it is part of the recovered
      number. Devanagari-digit writings converge to the same ASCII digit
      string.
- category: numeric_expressions
  phenomenon: roman
  canonical_form:
    type: generative
    instruction: >
      A value conventionally expressed with Roman numerals is written
      in normalized uppercase Roman-numeral notation using I, V, X, L,
      C, D, M. Spelled Hindi, Devanagari-digit, lowercase Roman, and
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
      by the canonical Hindi marker for their recovered address role,
      such as नंबर, गली, मार्ग, मकान नंबर, तल, मोहल्ला. Spoken and
      abbreviated realizations of the same role converge to that marker.
- category: symbols_markers
  phenomenon: biological
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic hi canonical rendering is
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
      Hindi written template, using the canonical structural label of
      the recovered citation type (e.g. अनुच्छेद, धारा, खंड, अधिनियम),
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
      No sufficiently deterministic hi canonical rendering is
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
