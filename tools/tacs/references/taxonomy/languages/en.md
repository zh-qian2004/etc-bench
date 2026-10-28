# en canonicalization taxonomy

This is the closed language-specific inventory for the language identified by this file's ISO 639-1 code. Language-agnostic numeric and symbol phenomena are defined in `../agnostic.md`.

Each description below is identical to the corresponding definition in the released ETC-Bench. Use it together with the category-level recognition methodology; canonical output forms are defined separately in `../../canonical-contracts/en.md`.

## abbreviations

Category methodology: Recover the contextually intended expansion and grammatical realization. This does not authorize rendering without an exact contract.

Semantic value: intended expansion and grammatical realization.

### `abbreviation`

Description: Abbreviations of titles, address suffixes, Latin phrases, and similar terms, such as Dr./Doctor, St./Street, and e.g./exempli gratia.

## orthographic_variants

Category methodology: Recover only genuinely equivalent lexical or character variants and their equivalence group. Do not select a target here.

Semantic value: lexical/character identity and equivalence group.

### `british_american_spelling`

Description: Differences between British and American spelling, such as colour/color, centre/center, and theatre/theater.

### `hyphen_variants`

Description: Variants with and without hyphens, such as e-mail/email and co-operate/cooperate.

### `diacritic_variants`

Description: Variants with and without diacritics, such as café/cafe, naïve/naive, and résumé/resume.

### `inflectional_consonant_doubling`

Description: Single vs double final consonant before inflectional suffixes such as -ed/-ing (often US single vs UK double), pronounced identically, e.g. traveled/travelled, canceled/cancelled, labeled/labelled, modeling/modelling, signaled/signalled.

## homophonic_substitutions

Category methodology: Recover only the stated equivalence relation and applicability. Do not collapse arbitrary homophones or select a representative here.

Semantic value: pronunciation group and contextually intended lexical item.

### `homophonic_names`

Description: Multiple spellings of homophonic proper names, such as John/Jon, Sara/Sarah, and Allen/Alan.

### `common_homophones`

Description: Common words that sound the same but are spelled differently; ASR cannot distinguish them from the audio alone, e.g. to/too/two, there/their/they're, flower/flour, right/write, see/sea, son/sun, pear/pair.
