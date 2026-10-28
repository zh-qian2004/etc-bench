# fa canonicalization taxonomy

This is the closed language-specific inventory for the language identified by this file's ISO 639-1 code. Language-agnostic numeric and symbol phenomena are defined in `../agnostic.md`.

Each description below is identical to the corresponding definition in the released ETC-Bench. Use it together with the category-level recognition methodology; canonical output forms are defined separately in `../../canonical-contracts/fa.md`.

## orthographic_variants

Category methodology: Recover only genuinely equivalent lexical or character variants and their equivalence group. Do not select a target here.

Semantic value: lexical/character identity and equivalence group.

### `persian_arabic_codepoint_variants`

Description: In Persian text, ک and ی may be replaced by the visually similar Arabic characters ك, ي, or ى without changing the word's pronunciation or identity. Examples: کتاب/كتاب, علی/علي, یک/يك.

### `affix_zwnj_spacing_variants`

Description: Prefixes, suffixes, and clitics may be joined to stems, separated by a zero-width non-joiner, or separated by an ordinary space. Examples: می‌روم/میروم/می روم, کتاب‌ها/کتابها/کتاب ها, خانه‌ام/خانه ام.

### `compound_boundary_spacing_variants`

Description: Inside compound words, fixed expressions, and reduplicative forms, components may be joined, separated by an ordinary space, or separated by a zero-width non-joiner; the preferred form often varies across dictionaries and typographic traditions. Examples: گفت‌وگو/گفتگو, جست‌وجو/جستجو, راه‌آهن/راه آهن.

### `ezafe_after_he_variants`

Description: When a word ending in silent ه takes the ezafe linker, it may be represented using a mark above ه, a separate ی, or a precomposed character. Examples: خانهٔ/خانه‌ی/خانۀ, نامهٔ/نامه‌ی/نامۀ, دربارهٔ/درباره‌ی/دربارۀ.

### `arabic_hamza_spelling_variants`

Description: In Arabic loanwords, hamza may be retained, omitted, or written on different carrier letters, resulting in the coexistence of traditional and modern spellings. Examples: تأثیر/تاثیر, مسئول/مسوول, جرئت/جرأت.

### `medial_y_glide_variants`

Description: In sequences such as /āy/, consonantal /y/ is generally written as ی in newer orthography, whereas older spelling often uses ئ with hamza. Examples: آیین/آئین, پاییز/پائیز, پایین/پائین.

### `merged_consonant_grapheme_variants`

Description: Several Arabic-derived letters are now homophonous in Persian, and some words have established alternative spellings because of differing etymological analyses or historical conventions. These homophonous letters should be handled as a unified mechanism. Examples: طوفان/توفان, اتاق/اطاق, زغال/ذغال.

### `final_alef_maqsura_variants`

Description: In some Arabic-derived words and proper names, final /ā/ may retain the Arabic ی/ى-style spelling or be rewritten as ا according to Persian pronunciation. Examples: حتی/حتا, عیسی/عیسا, موسی/موسا.

### `optional_diacritic_variants`

Description: Persian normally omits short vowels and other diacritics, but they may be written in educational materials, for disambiguation, or in formal typography. Tanwin in Arabic loanwords is also often either retained or omitted. Examples: مَن/من, کِتاب/کتاب, لطفاً/لطفا.

## homophonic_substitutions

Category methodology: Recover only the stated equivalence relation and applicability. Do not collapse arbitrary homophones or select a representative here.

Semantic value: pronunciation group and contextually intended lexical item.

### `proper_name_adjective_homophones`

Description: Personal names may be homophonous and identically written with ordinary adjectives; many Persian adjectives can also be used directly as personal names. Examples: شیرین (personal name/sweet), رها (personal name/free or released), آزاد (personal name/free).

### `arabic_consonant_letter_mergers`

Description: In Persian, several Arabic letters have merged into the same phoneme in modern standard pronunciation, creating homophonic ambiguity between different standard spellings. The main mergers are س/ص/ث→/s/, ز/ذ/ض/ظ→/z/, ت/ط→/t/, ه/ح→/h/, and ق/غ→/ɣ/ or similar sounds. Examples: ثواب/صواب, زغال/ذغال, طوفان/توفان.

### `ayn_hamza_weakening`

Description: In Arabic loanwords and some personal names, ع and ء are often weakened in modern spoken Persian to a very brief pause, a glottal stop, or no sound at all. Consequently, standard spellings containing ع/ء may sound identical or similar to spellings that omit the corresponding grapheme. Examples: تأثیر/تاثیر, مسئول/مسول, مؤسسه/موسسه.
