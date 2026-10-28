# id canonicalization taxonomy

This is the closed language-specific inventory for the language identified by this file's ISO 639-1 code. Language-agnostic numeric and symbol phenomena are defined in `../agnostic.md`.

Each description below is identical to the corresponding definition in the released ETC-Bench. Use it together with the category-level recognition methodology; canonical output forms are defined separately in `../../canonical-contracts/id.md`.

## abbreviations

Category methodology: Recover the contextually intended expansion and grammatical realization. This does not authorize rendering without an exact contract.

Semantic value: intended expansion and grammatical realization.

### `conventional_phrase_abbreviations`

Description: Frequent multiword phrases in formal written language may form conventional abbreviations, such as dll. → dan lain-lain, dsb. → dan sebagainya, and dst. → dan seterusnya.

### `informal_word_abbreviations`

Description: In text messages, chats, and social media, common words may be abbreviated by deleting vowels or retaining key letters, such as yg → yang, dgn → dengan, and utk → untuk.

## orthographic_variants

Category methodology: Recover only genuinely equivalent lexical or character variants and their equivalence group. Do not select a target here.

Semantic value: lexical/character identity and equivalence group.

### `optional_e_diacritics`

Description: The vowel e may be written with a diacritic as é, è, or ê when pronunciation needs to be indicated; omitting the diacritic remains valid in ordinary text, so the same word may occur in marked and unmarked forms. Examples include apel/apél meaning “apple,” teras/têras meaning “a central or senior figure,” and teras/téras meaning “terrace.”

### `legacy_spelling_in_proper_names`

Description: Letter combinations from spelling reforms predating modern Indonesian may legally remain in personal names, place names, institution names, and brand names, and may coexist with forms transcribed according to modern spelling. Common correspondences include oe/u, tj/c, dj/j, j/y, nj/ny, sj/sy, and ch/kh, as in Soekarno/Sukarno, Djakarta/Jakarta, and Tjokroaminoto/Cokroaminoto.

## homophonic_substitutions

Category methodology: Recover only the stated equivalence relation and applicability. Do not collapse arbitrary homophones or select a representative here.

Semantic value: pronunciation group and contextually intended lexical item.

### `given_name_common_noun_collision`

Description: In Indonesian, many given names differ from common nouns only by initial capitalization and are pronounced identically, such as Budi/budi (a name/virtue or reason), Intan/intan (a name/diamond), and Bayu/bayu (a name/wind).

### `given_name_adjective_collision`

Description: Some Indonesian given names are taken directly from words expressing qualities, so the proper name and the adjective are pronounced identically, such as Indah/indah (a name/beautiful), Suci/suci (a name/sacred or pure), and Agung/agung (a name/magnificent or exalted).

### `legacy_indonesian_orthography_names`

Description: Proper names may retain letter combinations from spelling reforms predating modern Indonesian, while the modern spelling represents the same pronunciation, such as Soeharto/Suharto (oe → u), Jusuf/Yusuf (old j → modern y), and Tjahjo/Cahyo (tj → c, j → y).

### `arabic_name_transliteration_variants`

Description: Names of Arabic origin may have multiple Indonesian spellings because of different transliteration systems, but they are pronounced identically according to Indonesian conventions, such as Syifa/Shifa, Fauzi/Fawzi, and Zaki/Dzaki.

### `noncontrastive_consonant_doubling_in_names`

Description: In Indonesian personal-name spelling, single and doubled consonants generally do not form a phonemic length contrast and may therefore be homophonous, such as Ana/Anna, Anisa/Annisa, and Nisa/Nissa.

### `final_y_for_i_in_names`

Description: Some modern given names use word-final y as a decorative or foreignized spelling, but it is actually pronounced /i/ and is homophonous with forms ending in i, such as Rizki/Rizky, Fadli/Fadly, and Doni/Dony.

### `foreign_name_spelling_vs_indonesianized_spelling`

Description: Foreign proper names may retain letter combinations from the original language or use Indonesianized phonemic spelling; in Indonesian pronunciation, the two forms are homophonous, such as Philip/Filip, Theresia/Teresia, and Christina/Kristina.

### `f_v_merger_in_names`

Description: In common Indonesian pronunciation, the foreign letter v is often realized as /f/, making proper names that differ only in f/v homophonous, such as Fina/Vina, Fani/Vani, and Fera/Vera.
