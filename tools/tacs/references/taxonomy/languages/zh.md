# zh canonicalization taxonomy

This is the closed language-specific inventory for the language identified by this file's ISO 639-1 code. Language-agnostic numeric and symbol phenomena are defined in `../agnostic.md`.

Each description below is identical to the corresponding definition in the released ETC-Bench. Use it together with the category-level recognition methodology; canonical output forms are defined separately in `../../canonical-contracts/zh.md`.

## orthographic_variants

Category methodology: Recover only genuinely equivalent lexical or character variants and their equivalence group. Do not select a target here.

Semantic value: lexical/character identity and equivalence group.

### `simplified_traditional`

Description: Conversion between Simplified Chinese and Traditional Chinese, two valid written forms of the same word.

### `variant_characters`

Description: Variant glyph forms of the same character (orthodox vs. popular / old vs. new shapes), identical pronunciation, e.g. 够/夠, 峰/峯, 污/汙, 群/羣, 烟/菸, 零/〇.

### `heterographic_words`

Description: Different written forms of the same word (heterographic variants), identical sound and meaning, e.g. 刻画/刻划, 交代/交待, 连接/联接, 含义/涵义, 人才/人材.

### `financial_capital_numerals`

Description: Lowercase Chinese numerals vs. the financial capital numerals used on official documents for amounts: 一/壹, 二/贰, 三/叁, 四/肆, 五/伍, 六/陆, 七/柒, 八/捌, 九/玖, 十/拾, 百/佰, 千/仟; pronunciation identical.

### `zero_character_variants`

Description: Two written forms of zero in Chinese numerals: 零 vs 〇 (e.g. 二〇二〇/二零二零, 一〇一/一零一); pronunciation identical.

## homophonic_substitutions

Category methodology: Recover only the stated equivalence relation and applicability. Do not collapse arbitrary homophones or select a representative here.

Semantic value: pronunciation group and contextually intended lexical item.

### `homophonic_names`

Description: References or proper names with the same pronunciation that ASR cannot distinguish from speech alone, such as homophonic personal names or the third-person pronoun tā, which may correspond to 他、她 or 它.

### `third_person_pronoun_script_variants`

Description: Homophonic script variants of the third-person pronoun tā: 他/她 for unknown or generic gender, and 它/他/她 for animals or personified pets.

### `surname_script_variants`

Description: Two common written forms of homophonic surnames: 傅/付, 阎/闫, 萧/肖, 蓝/兰, 戴/代; pronunciation identical, a family may use different forms in different contexts.

### `common_word_homophones`

Description: Different two-character words with identical pronunciation (homophonous words); speech alone cannot tell which characters were intended, e.g. 必须/必需, 权利/权力, 反映/反应, 形式/形势, 化妆/化装, 学历/学力, 终身/终生, 法制/法治.
