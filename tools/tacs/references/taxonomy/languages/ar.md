# ar canonicalization taxonomy

This is the closed language-specific inventory for the language identified by this file's ISO 639-1 code. Language-agnostic numeric and symbol phenomena are defined in `../agnostic.md`.

Each description below is identical to the corresponding definition in the released ETC-Bench. Use it together with the category-level recognition methodology; canonical output forms are defined separately in `../../canonical-contracts/ar.md`.

## orthographic_variants

Category methodology: Recover only genuinely equivalent lexical or character variants and their equivalence group. Do not select a target here.

Semantic value: lexical/character identity and equivalence group.

### `diacritic_presence_variants`

Description: The same word may be written with full or partial short-vowel and consonant diacritics, or with all such supplementary marks omitted; unvocalized writing is the norm in Modern Arabic. For example: كِتاب/كتاب, مُدَرِّس/مدرس, مَدْرَسَة/مدرسة.

### `hamza_seat_variants`

Description: In modern Arabic writing conventions, the letter serving as the seat of a medial hamza may vary in legally accepted or widely recognized spellings, especially between forms written on و, ئ, or independently. For example: مسؤول/مسئول, مئة/مائة, شؤون/شئون.

### `uthmani_imla_i_variants`

Description: The Uthmani script (الرسم العثماني) used in the Quran and religious texts differs systematically from modern orthography (الرسم الإملائي) through additions, omissions, or changes in letter forms. For example: الصلاة/الصلوة, الزكاة/الزكوة, هذا/هٰذا.

### `proper_name_compound_spacing`

Description: Arabic personal names containing components such as عبد may be written with spaces or as compounds according to naming conventions. For example: عبد الله/عبدالله, عبد الرحمن/عبدالرحمن, عبد العزيز/عبدالعزيز.

## homophonic_substitutions

Category methodology: Recover only the stated equivalence relation and applicability. Do not collapse arbitrary homophones or select a representative here.

Semantic value: pronunciation group and contextually intended lexical item.

### `final_alif_maqsura_variants`

Description: The word-final long vowel /aː/ may be represented by a regular alif (ا) or alif maqṣūra (ى), causing proper names, prepositions, or other lexical items to be phonologically identical but conventionally spelled differently. For example: علا (a personal name) / على (a preposition), رضا/رضى (common spelling variants of a personal name).

### `hamza_seat_orthographic_variants`

Description: The same glottal stop /ʔ/ and its syllabic context may have different spellings depending on the letter serving as the hamza seat or on whether the hamza is written explicitly, while the pronunciation remains the same. For example: مئة/مائة, مسؤول/مسئول, شؤون/شئون.

### `proper_name_common_noun_homophones`

Description: Personal names and common nouns or adjectives may have exactly the same pronunciation in Arabic, and Arabic generally does not distinguish between them by capitalization. For example: حسن (a personal name / “good, beautiful”), أمل (a personal name / “hope”), نور (a personal name / “light”).

### `proper_name_verb_homophones`

Description: Personal names and verb forms may have the same pronunciation in Modern Standard Arabic or in Saudi Arabic speech. For example: يحيى (a personal name / “he lives”), يزيد (a personal name / “he increases, is increasing”).
