# ru canonicalization taxonomy

This is the closed language-specific inventory for the language identified by this file's ISO 639-1 code. Language-agnostic numeric and symbol phenomena are defined in `../agnostic.md`.

Each description below is identical to the corresponding definition in the released ETC-Bench. Use it together with the category-level recognition methodology; canonical output forms are defined separately in `../../canonical-contracts/ru.md`.

## abbreviations

Category methodology: Recover the contextually intended expansion and grammatical realization. This does not authorize rendering without an exact contract.

Semantic value: intended expansion and grammatical realization.

### `common_multiword_graphic_abbreviations`

Description: Common connectives, explanatory expressions, or listing phrases are abbreviated using multiple initials followed by periods; when expanded, the full phrase is restored. For example: «т. е.» = «то есть», «и т. д.» = «и так далее», «т. н.» = «так называемый».

### `single_word_dot_truncations`

Description: A single common word is shortened to its initial part or stem and followed by a period; when read aloud, the full word is restored. For example: «напр.» = «например», «прибл.» = «приблизительно», «вкл.» = «включительно».

### `hyphenated_suffix_contractions`

Description: The beginning and end of a word are retained, while the middle is omitted and replaced with a hyphen. For example: «кол-во» = «количество», «кач-во» = «качество», «изд-во» = «издательство».

### `slash_graphic_abbreviations`

Description: A slash marks omitted material within a word or a multiword expression. For example: «б/у» = «бывший в употреблении», «ж/д» = «железнодорожный», «с/х» = «сельскохозяйственный».

### `context_dependent_homographic_abbreviations`

Description: The same abbreviated form followed by a period can correspond to different full words in different contexts and must be disambiguated from context. For example: «г.» can mean «год» or «город», «ст.» can mean «статья» or «станция», and «п.» can mean «пункт» or «посёлок».

### `doubled_plural_abbreviations`

Description: In traditional abbreviations, the plural is indicated by doubling a letter. For example: «гг.» = «годы/города/господа», «вв.» = «века», «пп.» = «пункты».

## orthographic_variants

Category methodology: Recover only genuinely equivalent lexical or character variants and their equivalence group. Do not select a target here.

Semantic value: lexical/character identity and equivalence group.

### `optional_yo_diacritic`

Description: In ordinary modern Russian texts, the two dots over the letter ё may usually be omitted, with е written instead. The same word may therefore have valid spellings both with and without the dots, such as жёлтый/желтый, берёза/береза, and шёпот/шепот.

### `lexical_vowel_doublets`

Description: A small number of words have dictionary-recognized alternative root-vowel spellings that cannot be freely generalized, such as тоннель/туннель “tunnel,” бивак/бивуак “bivouac,” and зарянка/зорянка “European robin.”

### `optional_glide_in_anglicisms`

Description: Some relatively recent English loanwords have standard spelling variants that differ in whether й is written before a vowel, such as плеер/плейер “player” and флаер/флайер “flyer.”

### `iskrenne_iskrenno_adverb_variants`

Description: Adverbs derived from искренний “sincere” have standard variants ending in -е and -о, such as искренне/искренно “sincerely” and неискренне/неискренно “insincerely.”

## homophonic_substitutions

Category methodology: Recover only the stated equivalence relation and applicability. Do not collapse arbitrary homophones or select a representative here.

Semantic value: pronunciation group and contextually intended lexical item.

### `given_name_common_noun_capitalization`

Description: Some given names are pronounced exactly like common nouns and are distinguished in writing primarily by capitalization. Examples include Вера (a given name)/вера “faith,” Роман (a given name)/роман “novel,” and Роза (a given name)/роза “rose.”

### `toponym_common_noun_capitalization`

Description: Some place names are homophonous with common nouns or common titles, so pronunciation alone does not indicate whether capitalization as a place name is required. Examples include Клин (a city)/клин “wedge,” Бор (a place name)/бор “pine forest,” and Дон (the Don River)/дон “a title of nobility.”

### `yo_omission_given_names`

Description: In written given names, ё is often replaced with е; the two spellings are usually pronounced identically or treated as forms of the same name, for example Семён/Семен, Фёдор/Федор, and Пётр/Петр.

### `yo_omission_surnames`

Description: In Russian surnames, ё is also often replaced with е, even in official texts, causing the same spoken surname to correspond to multiple written forms, such as Семёнов/Семенов, Фёдоров/Федоров, and Королёв/Королев.

### `yo_omission_pronouns`

Description: In pronouns and related pronominal forms, ё is often written as е, producing homophonous orthographic candidates, such as её/ее “her” and неё/нее “her” after a preposition.

### `homophonous_female_name_spelling_variants`

Description: Some female given names have different Russian-letter spellings but are homophonous in ordinary pronunciation, such as Майя/Мая, Тайя/Тая, and Кайя/Кая.

### `geminate_neutralization_in_names`

Description: In some varieties of spoken Russian, doubled consonants in foreign given names do not retain a consistent difference in duration, making double- and single-consonant spellings homophonous or nearly homophonous, such as Жанна/Жана, Инна/Ина, and Эмма/Эма.
