# id canonical contracts

This file declares exact `C(id, category, phenomenon)` contracts. The ISO 639-1 filename identifies the language. Follow `../canonicalization-method.md`.

Conventions: metalanguage and schema keys are English; `category`/`phenomenon` are benchmark identifiers; canonical literals are written in Standard Indonesian (Bahasa Indonesia, KBBI norm) exactly as the agent should output them. Each `instruction` states the canonical form of the phenomenon; it does not enumerate benchmark material or transcription-dependent cases. Category methodology never supplies a rendering fallback; without an exact applicable contract, retain the source span.

Shared rendering conventions:

```yaml
numeric_digits: ASCII 0-9
decimal_separator: "," (comma)
negative_sign: "-"
indonesian_orthography: Standard Indonesian, KBBI (Kamus Besar Bahasa Indonesia) norm
latin_width: halfwidth
identifier_latin_case: lowercase for natural-language words; uppercase for identifiers
phonetic_transcription:
  language: Standard Indonesian (formal reading norm)
  representation: broad phonemic IPA
  vowel_length: not marked (non-phonemic)
  stress: not marked (predictable, non-phonemic)
  connected_speech: no cross-word sandhi
  word_separator: single ASCII space
  wrapper: "/.../"
```

Canonical rendering may depend on the recovered semantic value and context inside the current record, but never on the source-side spelling, separator, symbol-versus-name choice, or another batch record.

## abbreviations

- category: abbreviations
  phenomenon: conventional_phrase_abbreviations
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span as the contextually recovered full
      Indonesian phrase, e.g. dll. → dan lain-lain, dsb. → dan
      sebagainya, dst. → dan seterusnya, a.n. → atas nama, u.p. → untuk
      perhatian. Apply the grammatical realization required by the
      surrounding syntax. If the expansion is ambiguous, retain the
      source span.
- category: abbreviations
  phenomenon: informal_word_abbreviations
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span as the recovered full Indonesian word,
      e.g. yg → yang, dgn → dengan, utk → untuk, krn → karena, tdk →
      tidak, sdh → sudah. Apply the grammatical realization required by
      the surrounding syntax. If the expansion is ambiguous, retain the
      source span.
## orthographic_variants

- category: orthographic_variants
  phenomenon: optional_e_diacritics
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the plain letter e; the é, è, ê
      spellings of the same Indonesian word converge to the
      diacritic-free KBBI form, e.g. apel, teras.
- category: orthographic_variants
  phenomenon: legacy_spelling_in_proper_names
  canonical_form:
    type: generative
    instruction: >
      Render the accepted proper name with its fully modernized EYD
      spelling of the recovered name. Pre-reform spellings converge to
      the corresponding modern letters: oe → u, dj → j, tj → c, sj →
      sy, and j → y. For example, Soedjono and Sudjono → Sujono;
      Soedibjo → Sudibjo; Tjandra → Candra; Tjahjono → Cahyono; Djoko →
      Joko; Djalal → Jalal; Joenoes → Yunus; Jusuf → Yusuf; Sjarif →
      Syarif; Sjamsuddin → Syamsuddin.
## homophonic_substitutions

- category: homophonic_substitutions
  phenomenon: given_name_common_noun_collision
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      name reading and the common-noun reading of the same letter
      sequence converge, e.g. Budi and budi → /ˈbudi/ with the
      predictable initial stress omitted → /budi/, Intan and intan →
      /intan/, Bayu and bayu → /bayu/. If the reading cannot be
      determined from the current record, retain the source span.
- category: homophonic_substitutions
  phenomenon: given_name_adjective_collision
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      name reading and the adjective reading of the same letter
      sequence converge, e.g. Indah and indah → /indah/, Suci and suci →
      /sutʃi/, Agung and agung → /aɡuŋ/. If the reading cannot be
      determined, retain the source span.
- category: homophonic_substitutions
  phenomenon: legacy_indonesian_orthography_names
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions,
      applying the legacy-orthography sound mappings (oe → /u/, tj →
      /tʃ/, dj → /dʒ/, j → /j/, nj → /ɲ/, sj → /ʃ/, ch → /x/ or /k/ per
      the recovered reading), e.g. Soeharto and Suharto converge to
      /suharto/, Jusuf and Yusuf to /jusuf/, Tjahjo and Cahyo to
      /tʃahjo/. If the reading cannot be determined, retain the source
      span.
- category: homophonic_substitutions
  phenomenon: arabic_name_transliteration_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the Indonesian readings of the variant transliterations
      transcribed identically (sy/sh → /ʃ/, au/aw → /aw/, z/dz → /z/),
      e.g. Syifa and Shifa → /ʃifa/, Fauzi and Fawzi → /fawzi/, Zaki
      and Dzaki → /zaki/. If the reading cannot be determined, retain
      the source span.
- category: homophonic_substitutions
  phenomenon: noncontrastive_consonant_doubling_in_names
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      consonant doubling not transcribed as length, e.g. Ana and Anna
      → /ana/, Anisa and Annisa → /anisa/, Nisa and Nissa → /nisa/.
      If the reading cannot be determined, retain the source span.
- category: homophonic_substitutions
  phenomenon: final_y_for_i_in_names
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the final y read as the vowel /i/, e.g. Rizki and Rizky →
      /riski/, Fadli and Fadly → /fadli/, Doni and Dony → /doni/. If
      the reading cannot be determined, retain the source span.
- category: homophonic_substitutions
  phenomenon: foreign_name_spelling_vs_indonesianized_spelling
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      the Indonesianized readings transcribed identically (ph → /f/,
      th → /t/, initial ch → /k/), e.g. Philip and Filip → /filip/,
      Theresia and Teresia → /teresia/, Christina and Kristina →
      /kristina/. If the reading cannot be determined, retain the
      source span.
- category: homophonic_substitutions
  phenomenon: f_v_merger_in_names
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions, with
      v transcribed as /f/, e.g. Fina and Vina → /fina/, Fani and Vani
      → /fani/, Fera and Vera → /fera/. If the record clearly
      distinguishes /v/, transcribe that distinction instead; otherwise,
      if the reading cannot be determined, retain the source span.
## numeric_expressions

- category: numeric_expressions
  phenomenon: cardinal
  canonical_form:
    type: generative
    instruction: >
      Quantities are written with ASCII digits. Spelled-out Indonesian
      number words and digits for the same quantity converge to the
      same ASCII digit string.
- category: numeric_expressions
  phenomenon: ordinal
  canonical_form:
    type: generative
    instruction: >
      Ranks are written with ASCII digits; the Indonesian ordinal word
      (e.g. kedua, kelima) of the same rank converges to the bare digit
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
      Complete dates are written as D month-name YYYY with one ASCII
      space between fields: ASCII digits with no leading zero for day,
      the Indonesian month name (Januari, Februari, Maret, April, Mei,
      Juni, Juli, Agustus, September, Oktober, November, Desember),
      and a four-digit year, e.g. 3 Juli 2026. Spelled-out and numeric
      writings of the same date converge to this form. Do not infer an
      unexpressed century or missing field.
- category: numeric_expressions
  phenomenon: time
  canonical_form:
    type: generative
    instruction: >
      Clock times with expressed minutes are written in 24-hour HH:MM
      form using ASCII digits and 「.」, e.g. 09.45. Resolve an expressed
      period-of-day word such as pagi, siang, sore, or malam into the
      24-hour value and omit that word from the canonical form. When
      only an hour is expressed, write the hour number alone without
      inventing minutes.
- category: numeric_expressions
  phenomenon: currency
  canonical_form:
    type: generative
    instruction: >
      Monetary amounts are written as an ASCII digit amount followed by
      the canonical Indonesian name of the recovered currency
      identity (rupiah for the Indonesian rupiah, dolar AS for the US
      dollar, euro for the euro, with a qualifier when the bare name is
      ambiguous, e.g. dolar Singapura). Symbol (Rp, $), abbreviation,
      and spoken-name inputs for the same currency converge to that
      name. Preserve explicitly expressed fractional precision.
- category: numeric_expressions
  phenomenon: unit
  canonical_form:
    type: generative
    instruction: >
      Measured values are written as an ASCII digit number, one ASCII
      space, and the canonical Indonesian name of the recovered unit
      identity (e.g. kilometer, meter, sentimeter, kilogram, gram, liter,
      mililiter, derajat Celsius, jam). Symbols, abbreviations (km, kg),
      and synonymous spoken unit names converge to the same unit name.
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
      C, D, M. Spelled Indonesian, lowercase Roman, and uppercase Roman
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
      by the canonical Indonesian marker for their recovered address
      role, such as Jalan, Nomor, Gang, RT, RW, Blok, Lantai. Spoken and
      abbreviated realizations of the same role converge to that marker.
- category: symbols_markers
  phenomenon: biological
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic id canonical rendering is
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
      Indonesian written template, using the canonical structural label
      of the recovered citation type (e.g. Pasal, Ayat, Undang-Undang),
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
      No sufficiently deterministic id canonical rendering is
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
