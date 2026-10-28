# de canonicalization taxonomy

This is the closed language-specific inventory for the language identified by this file's ISO 639-1 code. Language-agnostic numeric and symbol phenomena are defined in `../agnostic.md`.

Each description below is identical to the corresponding definition in the released ETC-Bench. Use it together with the category-level recognition methodology; canonical output forms are defined separately in `../../canonical-contracts/de.md`.

## abbreviations

Category methodology: Recover the contextually intended expansion and grammatical realization. This does not authorize rendering without an exact contract.

Semantic value: intended expansion and grammatical realization.

### `abbreviation`

Description: Expansion of German abbreviations into their full forms. The same expression may have an abbreviated and a fully written form with identical pronunciation. ASR may output either form, and both are equivalent. Examples: z.B./zum Beispiel, usw./und so weiter, bzw./beziehungsweise.

## orthographic_variants

Category methodology: Recover only genuinely equivalent lexical or character variants and their equivalence group. Do not select a target here.

Semantic value: lexical/character identity and equivalence group.

### `eszett_variants`

Description: Variants using Eszett (ß) or ss. These are two valid spellings of the same word with identical pronunciation. Examples: Straße/Strasse, Fuß/Fuss, Spaß/Spass.

### `umlaut_variants`

Description: Umlaut substitution variants. When ä/ö/ü cannot be entered, they are replaced with ae/oe/ue. These are two valid written forms of the same word with identical pronunciation. Examples: Müller/Mueller, schön/schoen, für/fuer.

### `foreign_word_spelling`

Description: Free spelling variants of foreign loanwords: the same word has two dictionary-recognized spellings with identical pronunciation. Examples: Joghurt/Jogurt, Phantasie/Fantasie, Delphin/Delfin, Graphik/Grafik, Telefon/Telephon.

### `native_lexical_variant_spellings`

Description: Native German words with two dictionary-recognized parallel spellings, usually differing in a vowel or an umlaut. Examples: aufwendig/aufwändig, Stengel/Stängel, Quentchen/Quäntchen.

### `compound_spacing_variants`

Description: Compound verbs, conjunctions and fixed constructions that may be written either together or separately. Both spellings are accepted and pronounced identically. Examples: kennenlernen/kennen lernen, sodass/so dass, radfahren/Rad fahren.

## homophonic_substitutions

Category methodology: Recover only the stated equivalence relation and applicability. Do not collapse arbitrary homophones or select a representative here.

Semantic value: pronunciation group and contextually intended lexical item.

### `homophonic_names`

Description: German surnames with identical pronunciation but different spellings. These spelling variants denote names that sound the same and therefore cannot be distinguished from speech by ASR. Examples: Meyer/Maier/Meier/Mayer (all pronounced /ˈmaɪ̯ɐ/), Schmidt/Schmitt/Schmid.

### `homophones`

Description: German common words (not proper names) that sound identical but are written differently; ASR cannot tell them apart from speech. Examples: das/dass, Lied/Lid, Waise/Weise, mal/Mahl, lehren/leeren.
