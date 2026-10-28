# ja canonical contracts

This file declares exact `C(ja, category, phenomenon)` contracts. The ISO 639-1 filename identifies the language. Follow `../canonicalization-method.md`.

Conventions: metalanguage and schema keys are English; `category`/`phenomenon` are benchmark identifiers; canonical literals are written in Standard Japanese exactly as the agent should output them. Each `instruction` states the canonical form of the phenomenon; it does not enumerate benchmark material or transcription-dependent cases. Category methodology never supplies a rendering fallback; without an exact applicable contract, retain the source span.

Shared rendering conventions:

```yaml
numeric_digits: ASCII 0-9; fullwidth digits converge to ASCII digits
decimal_separator: "."
negative_sign: "-"
japanese_script: Standard Japanese, modern kana usage (現代仮名遣い)
kanji_norm: Shinjitai (new form) as the default written norm
latin_width: halfwidth
identifier_latin_case: uppercase
phonetic_transcription:
  language: Standard Japanese (Tokyo norm)
  representation: broad phonemic IPA
  pitch_accent: not marked (not transcribed at this level)
  vowel_length: marked (phonemic)
  connected_speech: no cross-word sandhi; no sequential voicing rendered
  kana_to_ipa: standard gojūon correspondences, e.g. し /ɕi/, ち
    /tɕi/, つ /tsu/, ふ /ɸɯ/, ん transcribed per its contextual
    realization /n/, /m/, or /ɴ/
  word_separator: single ASCII space
  wrapper: "/.../"
```

Canonical rendering may depend on the recovered semantic value and context inside the current record, but never on the source-side spelling, separator, symbol-versus-name choice, or another batch record.

## orthographic_variants

- category: orthographic_variants
  phenomenon: shinjitai_kyujitai_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the shinjitai (new-form) kanji, e.g.
      国, 学, 体. The kyūjitai spelling of the same word converges to
      the shinjitai form.
- category: orthographic_variants
  phenomenon: kanji_itaiji_variants
  canonical_form:
    type: retain
    reason: >
      Itaiji variants such as 壺/壷 or 髙橋 carry identity-sensitive
      legal and personal-name value, and no general authority
      prescribes a unique standard form for every itaiji pair. Retain
      the source span rather than rewriting a possibly registered
      spelling.
- category: orthographic_variants
  phenomenon: kanji_hiragana_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word in hiragana, e.g. いう, できる, ある.
      The all-kanji spelling of the same native word converges to the
      hiragana form. Keep kanji where the standard convention
      requires kanji for the whole word; if the standard usage of the
      word genuinely admits both without a preferred form, retain the
      source span.
- category: orthographic_variants
  phenomenon: kanji_katakana_ateji_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted loanword in katakana, e.g. コーヒー, タバコ,
      ガラス. The kanji ateji spelling of the same loanword converges
      to the katakana form.
- category: orthographic_variants
  phenomenon: hiragana_katakana_script_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word in hiragana, e.g. ごみ, けが, ねこ. The
      katakana spelling of the same native word or naturalized loan
      converges to the hiragana form.
- category: orthographic_variants
  phenomenon: mazegaki_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the full kanji spelling of its
      dictionary headword, e.g. 改竄, 漏洩, 牽引. The mazegaki form of
      the same word converges to the full-kanji form.
- category: orthographic_variants
  phenomenon: alternative_kanji_spellings
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the kanji combination of its
      current primary dictionary headword, e.g. 障害, 交差, 知恵. The
      alternative kanji spelling of the same word converges to the
      primary form.
- category: orthographic_variants
  phenomenon: small_ke_counter_variants
  canonical_form:
    type: generative
    instruction: >
      Render the counter component of the accepted expression with the
      katakana 「カ」, e.g. 1カ月, 3カ所. The か, 箇, ヶ, and ケ writings of
      the same counter converge to the カ form.
- category: orthographic_variants
  phenomenon: wi_we_modernization_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name with the modern katakana イ and エ for
      ヰ and ヱ, e.g. エビス, イセキ. The old-kana spelling of the same
      name converges to the modern form.
- category: orthographic_variants
  phenomenon: shime_symbol_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span with the morpheme written in kanji or
      kana, e.g. 締切, 締め, しめ鯖. The 〆 symbol spelling of the same
      word converges to the kanji/kana form.
- category: orthographic_variants
  phenomenon: katakana_v_b_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted loanword with the traditional バ-row
      transcription of the foreign /v/, e.g. バイオリン, ビタミン,
      ベール. The ヴ-series spelling of the same loanword converges to
      the バ-row form.
- category: orthographic_variants
  phenomenon: katakana_extended_sound_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted loanword with its current primary dictionary
      katakana form. Where the primary form uses the extended sounds ティ
      or ディ (e.g. ティーム, ディジタル for words whose headword is so
      listed), the traditional チ/ジ spelling converges to it; where the
      primary form itself uses チ/ジ (e.g. チーム, デジタル), the extended
      spelling converges to it. If the primary form cannot be
      determined, retain the source span.
- category: orthographic_variants
  phenomenon: katakana_ei_long_vowel_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted loanword with its current primary dictionary
      katakana form for the English /eɪ/ diphthong. Where the primary
      form uses the long-vowel spelling エー (e.g. メーク, シェークスピア
      for words whose headword is so listed), the イ spelling converges
      to it; where the primary form uses イ (e.g. メイン, メイク), the
      エー spelling converges to it. If the primary form cannot be
      determined, retain the source span.
- category: orthographic_variants
  phenomenon: katakana_transliteration_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted loanword with its current primary dictionary
      katakana form, e.g. インターフェース, エンターテインメント,
      ダイヤモンド. Alternative transliterations of the same loanword
      converge to the primary form. If the primary form cannot be
      determined, retain the source span.
- category: orthographic_variants
  phenomenon: katakana_middle_dot_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted multi-component loanword or foreign name with
      the katakana middle dot 「・」 between its components, e.g.
      ケース・バイ・ケース, ニュー・ヨーク, レオナルド・ダ・ヴィンチ. The
      dot-free spelling of the same expression converges to the dotted
      form.
- category: orthographic_variants
  phenomenon: latin_katakana_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted letter-word with its katakana reading, e.g.
      AI → エーアイ, CD → シーディー, Tシャツ → ティーシャツ. The
      Latin-letter spelling of the same letter-word converges to the
      katakana reading. If the reading cannot be determined, retain
      the source span.
- category: orthographic_variants
  phenomenon: halfwidth_fullwidth_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span in fullwidth kana and fullwidth Latin
      letters; halfwidth kana with combining voiced marks merge into
      fullwidth voiced kana, e.g. ｶﾞ → ガ. Fullwidth Latin letters and
      digits converge to their halfwidth equivalents only when they are
      part of an identifier; within Japanese words, kana converge to
      fullwidth.

## homophonic_substitutions

- category: homophonic_substitutions
  phenomenon: given_name_kanji_homophones
  canonical_form:
    type: generative
    instruction: >
      Render the accepted given name's contextually determined
      pronunciation in broad phonemic IPA under the shared phonetic
      conventions, e.g. 直樹, 尚樹, 直紀 with reading なおき converge to
      /naoki/. If the reading cannot be determined from the current
      record, retain the source span.
- category: homophonic_substitutions
  phenomenon: surname_kanji_homophones
  canonical_form:
    type: generative
    instruction: >
      Render the accepted surname's contextually determined
      pronunciation in broad phonemic IPA under the shared phonetic
      conventions, e.g. 酒井, 坂井, 堺 with reading さかい converge to
      /sakaꜛi/ as /sakai/. If the reading cannot be determined, retain
      the source span.
- category: homophonic_substitutions
  phenomenon: saito_variant_surnames
  canonical_form:
    type: generative
    instruction: >
      Render the accepted surname's contextually determined
      pronunciation in broad phonemic IPA under the shared phonetic
      conventions: 斎藤, 斉藤, 齋藤, 齊藤 with reading さいとう converge
      to /saitoː/. If the reading cannot be determined, retain the
      source span.
- category: homophonic_substitutions
  phenomenon: place_name_proper_name_collision
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      place-name reading and the personal-name reading of the same
      phonological word converge, e.g. 市川 as a place or surname
      converges to /itɕikaꜛwa/ as /itɕikawa/. If the reading cannot be
      determined, retain the source span.
- category: homophonic_substitutions
  phenomenon: first_person_pronoun_script_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted pronoun's contextually determined
      pronunciation in broad phonemic IPA under the shared phonetic
      conventions: 私 and わたし converge to /watɕi/, 僕 and ぼく to
      /bokɯ/, 俺 and おれ to /oɾe/, 我 and われ to /waɾe/.
- category: homophonic_substitutions
  phenomenon: second_person_pronoun_script_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted pronoun's contextually determined
      pronunciation in broad phonemic IPA under the shared phonetic
      conventions: あなた and 貴方 converge to /anata/, きみ and 君 to
      /kimʲi/ as /kimi/, おまえ and お前 to /omaꜛe/ as /omae/.
- category: homophonic_substitutions
  phenomenon: third_person_pronoun_script_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted pronoun's contextually determined
      pronunciation in broad phonemic IPA under the shared phonetic
      conventions: 彼 and かれ converge to /kaɾe/, 彼女 and かのじょ to
      /kanoɕo/ as /kanojo/, あの人 and あのひと to /anohito/.
- category: homophonic_substitutions
  phenomenon: demonstrative_pronoun_script_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted demonstrative's contextually determined
      pronunciation in broad phonemic IPA under the shared phonetic
      conventions: ここ and 此処 converge to /koko/, そこ and 其処 to
      /soko/, こちら and 此方 to /kotɕiɾa/, あちら and 彼方 to
      /atɕiɾa/, どちら and 何方 to /dotɕiɾa/.
- category: homophonic_substitutions
  phenomenon: interrogative_pronoun_script_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted interrogative's contextually determined
      pronunciation in broad phonemic IPA under the shared phonetic
      conventions: だれ and 誰 converge to /daɾe/, どなた and 何方 to
      /donata/, どこ and 何処 to /doko/, いつ and 何時 to /itsɯ/ as
      /itsu/.
- category: homophonic_substitutions
  phenomenon: jibun_person_reference_ambiguity
  canonical_form:
    type: generative
    instruction: >
      Render the accepted span's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions:
      自分 with its reading じぶん converges to /ɕibɯɴ/ as /ɕibuɴ/
      regardless of whether the intended referent is first person,
      second person, or reflexive.

## numeric_expressions

- category: numeric_expressions
  phenomenon: cardinal
  canonical_form:
    type: generative
    instruction: >
      Quantities are written with ASCII digits. Spelled-out Japanese
      number words, kanji numerals, and fullwidth digits for the same
      quantity converge to the same ASCII digit string.
- category: numeric_expressions
  phenomenon: ordinal
  canonical_form:
    type: generative
    instruction: >
      Ranks are written with ASCII digits; the Japanese ordinal form
      (第N) of the same rank converges to the bare digit string of the
      rank value.
- category: numeric_expressions
  phenomenon: decimal
  canonical_form:
    type: generative
    instruction: >
      Decimal values are written with ASCII digits and 「.」 as the
      decimal separator, preserving sign, digits, and written
      precision. Fullwidth-digit writings of the same value converge
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
      Complete Gregorian dates are written as YYYY年M月D日 with ASCII
      digits. The year has four digits; month and day have no leading
      zero. Do not infer an unexpressed century or missing field.
- category: numeric_expressions
  phenomenon: time
  canonical_form:
    type: generative
    instruction: >
      Clock times with expressed minutes are written in 24-hour HH:MM
      form using ASCII digits and 「:」. Resolve an expressed period-of-day
      word such as 朝, 昼, 夜, or 午前/午後 into the 24-hour value and
      omit that word from the canonical form. When only an hour is
      expressed, write the hour number alone without inventing minutes.
- category: numeric_expressions
  phenomenon: currency
  canonical_form:
    type: generative
    instruction: >
      Monetary amounts are written as an ASCII digit amount followed by
      the canonical Japanese name of the recovered currency identity
      (円 for the Japanese yen, ドル for the US dollar, ユーロ for the
      euro, with a qualifier when the bare name is ambiguous, e.g.
      豪ドル). Symbol, abbreviation, and spoken-name inputs for the same
      currency converge to that name. Preserve explicitly expressed
      fractional precision.
- category: numeric_expressions
  phenomenon: unit
  canonical_form:
    type: generative
    instruction: >
      Measured values are written as an ASCII digit number followed by
      the canonical Japanese name of the recovered unit identity (e.g.
      キロメートル, メートル, センチメートル, キログラム, グラム, リットル,
      ミリリットル, 摂氏). Symbols, abbreviations (km, kg), and
      synonymous spoken unit names converge to the same unit name.
- category: numeric_expressions
  phenomenon: phone
  canonical_form:
    type: generative
    instruction: >
      Telephone numbers are written as one contiguous ASCII digit string
      with all presentation grouping separators removed. Preserve a
      leading international 「+」 when it is part of the recovered
      number. Fullwidth-digit writings converge to the same ASCII digit
      string.
- category: numeric_expressions
  phenomenon: roman
  canonical_form:
    type: generative
    instruction: >
      A value conventionally expressed with Roman numerals is written
      in normalized uppercase Roman-numeral notation using I, V, X, L,
      C, D, M. Spelled Japanese, kanji-numeral, lowercase Roman, and
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
      by the canonical Japanese marker for their recovered address
      role, such as 丁目, 番地, 号, 室, 階, 番. Spoken and abbreviated
      realizations of the same role converge to that marker.
- category: symbols_markers
  phenomenon: biological
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic ja canonical rendering is
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
      Japanese written template, using the canonical structural label
      of the recovered citation type (e.g. 条, 項, 号, 平成/令和 for era
      years), ASCII digits, and halfwidth uppercase Latin letters where
      the citation contains them. Typographic variants converge to the
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
      No sufficiently deterministic ja canonical rendering is
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
