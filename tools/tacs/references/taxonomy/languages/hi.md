# hi canonicalization taxonomy

This is the closed language-specific inventory for the language identified by this file's ISO 639-1 code. Language-agnostic numeric and symbol phenomena are defined in `../agnostic.md`.

Each description below is identical to the corresponding definition in the released ETC-Bench. Use it together with the category-level recognition methodology; canonical output forms are defined separately in `../../canonical-contracts/hi.md`.

## orthographic_variants

Category methodology: Recover only genuinely equivalent lexical or character variants and their equivalence group. Do not select a target here.

Semantic value: lexical/character identity and equivalence group.

### `q_nukta_variants`

Description: In Persian-Arabic loanwords, /q/ may be written with the nukta as “क़”, but the nukta is often omitted, yielding “क”. Examples: क़िला/किला, क़ीमत/कीमत, क़ायदा/कायदा।

### `kh_nukta_variants`

Description: In Persian-Arabic loanwords, /x/ may be written as “ख़”, but the nukta is often omitted, yielding “ख”. Examples: ख़बर/खबर, ख़त्म/खत्म, ख़ास/खास।

### `gh_nukta_variants`

Description: The voiced velar fricative /ɣ/ in loanwords may be written as “ग़”, but it is also often written as “ग”. Examples: ग़रीब/गरीब, ग़लत/गलत, ग़ायब/गायब।

### `z_nukta_variants`

Description: The /z/ in loanwords may be written as “ज़”, but the nukta is often omitted, yielding “ज”. Examples: ज़रूरी/जरूरी, ज़िंदगी/जिंदगी, ज़मीन/जमीन।

### `f_nukta_variants`

Description: The /f/ in loanwords may be written as “फ़”, but the nukta is often omitted, yielding “फ”. Examples: फ़ायदा/फायदा, फ़र्क/फर्क, फ़िल्म/फिल्म।

### `chandrabindu_anusvara_variants`

Description: When marking vowel nasalization, the standard chandrabindu “ँ” is often replaced by the anusvara “ं”. Examples: माँ/मां, हँसना/हंसना, गाँव/गांव।

### `anusvara_homorganic_nasal_variants`

Description: Before a consonant, a nasal may be written with the anusvara “ं” or as the corresponding homorganic nasal consonant. Examples: हिंदी/हिन्दी, संपत्ति/सम्पत्ति, अंतर/अन्तर।

### `iye_ie_variants`

Description: In the endings of some verbs and related forms, “ि‍ए” and “िये” spellings both occur; the insertion of “य” varies in actual usage. Examples: किए/किये, लिए/लिये, दिए/दिये।

### `yi_i_variants`

Description: The endings of some words and feminine or past-tense verb forms may be written with either “ई” or “यी”. Examples: नई/नयी, गई/गयी, आई/आयी।

### `visarga_retention_variants`

Description: The Sanskrit-derived visarga “ः” is often retained in modern Hindi, but it is also commonly omitted. Examples: दुःख/दुख, निःशब्द/निशब्द, निःस्वार्थ/निस्वार्थ।

### `foreign_rounded_vowel_variants`

Description: The /ɔ/ or a similar short rounded vowel in English and other foreign words may be represented by “ऑ”, but is also often represented by “आ” or “ओ”. Examples: कॉलेज/कालेज, ऑफिस/आफिस, डॉक्टर/डाक्टर।

## homophonic_substitutions

Category methodology: Recover only the stated equivalence relation and applicability. Do not collapse arbitrary homophones or select a representative here.

Semantic value: pronunciation group and contextually intended lexical item.

### `z_j_name_merger`

Description: The foreign sound /z/ and the native sound /dʒ/ merge in the pronunciation of many Hindi speakers, making proper names spelled with the nukta and without the nukta homophonous. Examples: ज़ाकिर/जाकिर, ज़ुबैर/जुबैर, ज़हीर/जहीर।

### `f_ph_name_merger`

Description: The foreign sound /f/ and the Hindi aspirated bilabial stop /pʰ/ merge in the pronunciation of some speakers, making proper names containing फ़ and those containing फ homophonous. Examples: फ़ैसल/फैसल, फ़रहान/फरहान, फ़िरोज़/फिरोज़।

### `kh_kh_nukta_name_merger`

Description: The foreign sound /x/ and the Hindi aspirated velar stop /kʰ/ commonly merge in Hindi, making proper names spelled with ख़ and ख homophonous. Examples: ख़ान/खान, ख़ालिद/खालिद, ख़ुर्शीद/खुर्शीद।

### `q_k_name_merger`

Description: The foreign sound /q/ and the Hindi velar stop /k/ frequently merge in most spoken Hindi, making proper names spelled with क़ and क homophonous. Examples: क़ासिम/कासिम, क़ुरैशी/कुरैशी, क़मर/कमर।

### `gh_g_name_merger`

Description: The foreign sound /ɣ/ and the Hindi voiced velar stop /ɡ/ merge in the pronunciation of many speakers, making proper names spelled with ग़ and ग homophonous. Examples: ग़ालिब/गालिब, ग़नी/गनी, ग़फ़ूर/गफूर।

### `colloquial_demonstrative_pronoun_spelling`

Description: In colloquial Hindi, the standard and informal spellings of demonstrative pronouns often undergo vowel reduction, loss of weak consonants, and morphological merging, especially वह/वो and यह/ये; वे/वो may also be pronounced identically or nearly identically as [voː] and [jeː]. ASR output may therefore not determine the standard spelling from pronunciation alone.
