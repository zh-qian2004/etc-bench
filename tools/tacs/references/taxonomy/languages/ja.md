# ja canonicalization taxonomy

This is the closed language-specific inventory for the language identified by this file's ISO 639-1 code. Language-agnostic numeric and symbol phenomena are defined in `../agnostic.md`.

Each description below is identical to the corresponding definition in the released ETC-Bench. Use it together with the category-level recognition methodology; canonical output forms are defined separately in `../../canonical-contracts/ja.md`.

## orthographic_variants

Category methodology: Recover only genuinely equivalent lexical or character variants and their equivalence group. Do not select a target here.

Semantic value: lexical/character identity and equivalence group.

### `shinjitai_kyujitai_variants`

Description: Shinjitai and kyujitai can provide different written forms of the same word, such as 「国／國」「学／學」「体／體」.

### `kanji_itaiji_variants`

Description: A kanji may have variant forms that do not follow the usual shinjitai–kyujitai correspondence, producing word-form variants such as 「壺／壷」「竈／竃」「籠／篭」.

### `kanji_hiragana_variants`

Description: The same native Japanese or Japanized word may be written in kanji or hiragana, such as 「言う／いう」「出来る／できる」「有る／ある」.

### `kanji_katakana_ateji_variants`

Description: Some loanwords or historical borrowings have both kanji and katakana spellings, such as 「珈琲／コーヒー」「煙草／タバコ」「硝子／ガラス」.

### `hiragana_katakana_script_variants`

Description: Some words may be written in either hiragana or katakana depending on style, such as 「ごみ／ゴミ」「けが／ケガ」「ねこ／ネコ」.

### `mazegaki_variants`

Description: To avoid difficult kanji or for similar reasons, part of a word may be rewritten in hiragana, producing mixed-script spellings (mazegaki) such as 「改竄／改ざん」「漏洩／漏えい」「牽引／けん引」.

### `alternative_kanji_spellings`

Description: The same word may be written with different kanji combinations that are not merely variant character forms, such as 「障碍／障害」「交叉／交差」「智慧／知恵」.

### `small_ke_counter_variants`

Description: The counting element representing 「か／箇」 may be written as 「か、カ、箇、ヶ、ケ」 and other forms, as in 「一か月／一カ月／一箇月／一ヶ月」 and 「箇所／か所／カ所／ヶ所」.

### `wi_we_modernization_variants`

Description: The obsolete katakana 「ヰ、ヱ」 and their modern equivalents 「イ、エ」 may occur as parallel spellings in historical names or brands, such as 「ヱビス／エビス」「ヰセキ／イセキ」「ヱヴァ／エヴァ」.

### `shime_symbol_variants`

Description: The ligature-like symbol "〆" can alternate with "締" or "しめ" in writing, as in "締切／〆切," "締め／〆," and "しめ鯖／〆鯖."

### `katakana_v_b_variants`

Description: Foreign /v/ sounds in loanwords may be represented using the ヴ series or the traditional バ row, as in "ヴァイオリン／バイオリン," "ヴィタミン／ビタミン," and "ヴェール／ベール."

### `katakana_extended_sound_variants`

Description: Foreign sounds may be represented either by forms closer to the traditional Japanese phonological system or by more precise modern katakana combinations, as in "チーム／ティーム," "デジタル／ディジタル," and "スチーム／スティーム."

### `katakana_ei_long_vowel_variants`

Description: Diphthongs or /eɪ/ in the source language may be written using an イ sequence or a long vowel, as in "メイン／メーン," "メイク／メーク," and "シェイクスピア／シェークスピア."

### `katakana_transliteration_variants`

Description: The same loanword may also have multiple katakana spellings due to different transliteration conventions, as in "インターフェース／インターフェイス," "エンターテインメント／エンターテインメント," and "ダイヤモンド／ダイアモンド."

### `katakana_middle_dot_variants`

Description: The middle dot in multiword loan expressions or foreign personal names may be retained or omitted, as in "ケース・バイ・ケース／ケースバイケース," "ニュー・ヨーク／ニューヨーク," and "レオナルド・ダ・ヴィンチ／レオナルドダヴィンチ."

### `latin_katakana_variants`

Description: Letter names or abbreviations may be written directly in Latin letters or phonetically in katakana, as in "AI／エーアイ," "CD／シーディー," and "Tシャツ／ティーシャツ."

### `halfwidth_fullwidth_variants`

Description: In numeric text, the same term may use full-width or half-width characters, as in "カタカナ／ｶﾀｶﾅ," "パソコン／ﾊﾟｿｺﾝ," and "AI／ＡＩ."

## homophonic_substitutions

Category methodology: Recover only the stated equivalence relation and applicability. Do not collapse arbitrary homophones or select a representative here.

Semantic value: pronunciation group and contextually intended lexical item.

### `given_name_kanji_homophones`

Description: Japanese given names often have multiple homophonous kanji spellings, and the specific name cannot be determined from speech alone. For example, "なおき" may be written as "直樹," "尚樹," or "直紀," while "ゆうき" may be written as "勇気," "優希," or "悠希."

### `surname_kanji_homophones`

Description: Japanese surnames may have the same pronunciation but different kanji spellings. For example, "さかい" may be written as "酒井," "坂井," or "堺," while "はしもと" may be written as "橋本" or "橋元."

### `saito_variant_surnames`

Description: The surname "Saito" has many homophonous kanji spellings that have historically coexisted, such as 「斎藤」「斉藤」「齋藤」「齊藤」. Speech alone cannot determine which character forms should be used.

### `place_name_proper_name_collision`

Description: The same reading may refer to proper names in different categories. For example, 「いちかわ」 may refer to the place name 「市川」 in Chiba Prefecture or to a person with the surname 「市川」; 「やまと」 may refer to the place name or historical regional name 「大和」.

### `first_person_pronoun_script_variants`

Description: First-person pronouns commonly appear in homophonous kanji, hiragana, or mixed-script forms, such as 「私／わたし」「僕／ぼく」「俺／おれ」. Speech cannot determine which written form should be used during text normalization.

### `second_person_pronoun_script_variants`

Description: Second-person pronouns have homophonous kanji and kana spellings, such as 「あなた／貴方」「きみ／君」「おまえ／お前」. These written choices cannot be distinguished from speech.

### `third_person_pronoun_script_variants`

Description: Third-person pronouns also have homophonous kanji and kana forms, such as 「彼／かれ」「彼女／かのじょ」「あの人／あのひと」. Without orthographic cues, ASR output cannot determine the normalized form.

### `demonstrative_pronoun_script_variants`

Description: Demonstrative pronouns and demonstrative location words have homophonous spelling variants, such as 「ここ／此処」「そこ／其処」「こちら／此方」「あちら／彼方」.

### `interrogative_pronoun_script_variants`

Description: Interrogative referential words also have homophonous kanji and kana forms, such as 「だれ／誰」「どなた／何方」「どこ／何処」.

### `jibun_person_reference_ambiguity`

Description: In modern Japanese, 「自分（じぶん）」 may function as a reflexive expression or as a first-person pronoun in some dialects and in sports, military, and male colloquial speech. In certain contexts, it may also refer to the second person.
