# bn canonical contracts

This file declares exact `C(bn, category, phenomenon)` contracts. The ISO 639-1 filename identifies the language. Follow `../canonicalization-method.md`.

Conventions: metalanguage and schema keys are English; `category`/`phenomenon` are benchmark identifiers; canonical literals are written in Standard Bangla as used in Bangladesh exactly as the agent should output them. Each `instruction` states the canonical form of the phenomenon; it does not enumerate benchmark material or transcription-dependent cases. Category methodology never supplies a rendering fallback; without an exact applicable contract, retain the source span.

Shared rendering conventions:

```yaml
numeric_digits: ASCII 0-9; Bengali digits converge to ASCII digits
decimal_separator: "."
negative_sign: "-"
bangla_script: Standard Bangla, Bangladesh written norm
latin_width: halfwidth
identifier_latin_case: uppercase
phonetic_transcription:
  language: Standard Bangla as spoken in Bangladesh (formal reading style)
  representation: broad phonemic IPA
  vowel_length: marked (phonemic)
  tone: not applicable
  stress: not marked (non-phonemic)
  connected_speech: no cross-word sandhi; vowel length distinctions are
    neutralized where the phenomenon's equivalence relation states so
  word_separator: single ASCII space
  wrapper: "/.../"
```

Canonical rendering may depend on the recovered semantic value and context inside the current record, but never on the source-side spelling, separator, symbol-versus-name choice, or another batch record.

## orthographic_variants

- category: orthographic_variants
  phenomenon: nukta_flap_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the precomposed letters ড় and ঢ়
      for the retroflex flaps; the decomposed ড+nukta and ঢ+nukta
      sequences converge to their precomposed forms.
- category: orthographic_variants
  phenomenon: historical_i_length_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the short vowel sign ই (-ি) in the
      affected position; the historical long spelling with ঈ (-ী)
      converges to the short spelling, e.g. বাড়ি, শ্রেণি.
- category: orthographic_variants
  phenomenon: historical_u_length_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the short vowel sign উ (-ু) in the
      affected position; the historical long spelling with ঊ (-ূ)
      converges to the short spelling, e.g. রুপা, রুপালি, দুর্গাপুজা.
- category: orthographic_variants
  phenomenon: khanda_ta_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted word with the explicit consonant cluster ত্
      (khanda-ta as ত্ in cluster position); the khanda-ta character ৎ
      converges to the cluster spelling with ত্, e.g. উত্সব, সত্কার.
- category: orthographic_variants
  phenomenon: loanword_vowel_adaptation
  canonical_form:
    type: generative
    instruction: >
      Render the accepted Arabic- or Persian-origin loanword with its
      Standard Bangla written form; competing vowel adaptations of the
      recovered word converge to that form. The standard spellings use
      the short vowel উ in the o/u alternation, the short vowel sign
      ই (-ি), and the precomposed letter য়, e.g. কোরআন and কোরান →
      কুরআন; কোরবানি and কোরবানী → কুরবানি; ফেব্রুয়ারি and জানুয়ারি
      are written with precomposed য় and short final -ি (ফেব্রুয়ারী
      and জানুয়ারী, and the decomposed য় spellings of the same words,
      converge accordingly); ইরানী → ইরানি; সৌদী →
      সৌদি.
## homophonic_substitutions

- category: homophonic_substitutions
  phenomenon: i_ii_name_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      historical i-length contrast is not transcribed; মিনা and মীনা
      converge to /mina/, রহিম and রহীম to /ɾohim/.
- category: homophonic_substitutions
  phenomenon: u_uu_name_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      historical u-length contrast is not transcribed; পূজা and পুজা
      converge to /pudʒa/, রূপা and রুপা to /ɾupa/.
- category: homophonic_substitutions
  phenomenon: n_nukta_name_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      dental ন and retroflex ণ are transcribed with the same dental /n/;
      অরুণ and অরুন converge to /oɾun/.
- category: homophonic_substitutions
  phenomenon: sha_ssha_name_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      two sibilant letters are transcribed with the same phoneme /ʃ/;
      সুশমা and সুষমা converge to /suʃma/.
- category: homophonic_substitutions
  phenomenon: ja_ya_name_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. In
      word-initial position য and জ converge to /dʒ/; জাহিদ and যাহিদ
      converge to /dʒahid/.
- category: homophonic_substitutions
  phenomenon: ri_ri_vowel_name_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions.
      Vowel-sign ঋ and the sequence রি converge to /ɾi/; ঋতু and রিতু
      converge to /ɾitu/.
- category: homophonic_substitutions
  phenomenon: ai_aae_name_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      vowel-sign sequences আই and াঈ converge to /ai/; সাইদ and সাঈদ
      converge to /said/.
- category: homophonic_substitutions
  phenomenon: abdul_cluster_spelling_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      spelled-out cluster আব্দ- and the simplified আবদ- converge to
      /abdu/; আবদুল and আব্দুল converge to /abdul/.
- category: homophonic_substitutions
  phenomenon: orthographic_y_glide_name_variants
  canonical_form:
    type: generative
    instruction: >
      Render the accepted name's contextually determined pronunciation
      in broad phonemic IPA under the shared phonetic conventions. The
      য় and য spellings of the same /y/ sound converge to the same
      transcription, e.g. বিজয় and বিজয় to /bidʒoj/.
## numeric_expressions

- category: numeric_expressions
  phenomenon: cardinal
  canonical_form:
    type: generative
    instruction: >
      Quantities are written with ASCII digits. Spelled-out Bangla
      number words, Bengali digits, and ASCII digits for the same
      quantity converge to the same ASCII digit string.
- category: numeric_expressions
  phenomenon: ordinal
  canonical_form:
    type: generative
    instruction: >
      Ranks are written with ASCII digits; the ordinal suffix, its
      spoken form, and digit writings of the same rank converge to the
      bare digit string of the rank value.
- category: numeric_expressions
  phenomenon: decimal
  canonical_form:
    type: generative
    instruction: >
      Decimal values are written with ASCII digits and 「.」 as the
      decimal separator, preserving sign, digits, and written
      precision. Bengali-digit or Bengali-decimal-separator writings of
      the same value converge to this form.
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
      Complete Gregorian dates are written as D MMMM, YYYY with ASCII
      digits: the day with no leading zero, the Bangla month name
      (জানুয়ারি, ফেব্রুয়ারি, মার্চ, এপ্রিল, মে, জুন, জুলাই, আগস্ট,
      সেপ্টেম্বর, অক্টোবর, নভেম্বর, ডিসেম্বর), an ASCII comma, one ASCII
      space, and the four-digit year. Do not infer an unexpressed
      century or missing field.
- category: numeric_expressions
  phenomenon: time
  canonical_form:
    type: generative
    instruction: >
      Clock times with expressed minutes are written in 12-hour h:mm
      form using ASCII digits and 「:」, followed by one ASCII space and
      the Bangla period marker পূর্বাহ্ন (before noon) or অপরাহ্ন (after
      noon) as required by the recovered time. Resolve a spoken
      period-of-day phrase such as সকাল or রাত into the 12-hour value
      and the corresponding marker. When only an hour is expressed,
      write the hour number alone without inventing minutes.
- category: numeric_expressions
  phenomenon: currency
  canonical_form:
    type: generative
    instruction: >
      Monetary amounts are written as an ASCII digit amount followed by
      the canonical Bangla name of the recovered currency identity
      (টাকা for the Bangladeshi taka, ডলার for the US dollar, ইউরো for
      the euro, রুপি for the Indian rupee, পাউন্ড for the pound
      sterling, with a qualifier when the bare name is ambiguous, e.g.
      সৌদি রিয়াল). Symbol, abbreviation, and spoken-name inputs for
      the same currency converge to that name. Preserve explicitly
      expressed fractional precision.
- category: numeric_expressions
  phenomenon: unit
  canonical_form:
    type: generative
    instruction: >
      Measured values are written as an ASCII digit number, one ASCII
      space, and the canonical Bangla name of the recovered unit
      identity (e.g. কিলোমিটার, মিটার, সেন্টিমিটার, কিলোগ্রাম, গ্রাম,
      লিটার, মিলিলিটার, ডিগ্রি সেলসিয়াস, কিলোমেট্রিক). Symbols,
      abbreviations, and synonymous spoken unit names converge to the
      same unit name.
- category: numeric_expressions
  phenomenon: phone
  canonical_form:
    type: generative
    instruction: >
      Telephone numbers are written as one contiguous ASCII digit string
      with all presentation grouping separators removed. Preserve a
      leading international 「+」 when it is part of the recovered
      number. Bengali-digit writings converge to the same ASCII digit
      string.
- category: numeric_expressions
  phenomenon: roman
  canonical_form:
    type: generative
    instruction: >
      A value conventionally expressed with Roman numerals is written
      in normalized uppercase Roman-numeral notation using I, V, X, L,
      C, D, M. Spelled Bangla, Bangla-digit, lowercase Roman, and
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
      by the canonical Bangla marker for their recovered address role,
      such as নম্বর, রোড, ব্লক, সেকশন, ফ্ল্যাট, তলা. Spoken and
      abbreviated realizations of the same role converge to that
      marker.
- category: symbols_markers
  phenomenon: biological
  canonical_form:
    type: retain
    reason: >
      No sufficiently deterministic bn canonical rendering is
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
      Bangla written template, using the canonical structural label of
      the recovered citation type (e.g. ধারা, অনুচ্ছেদ, আইন), ASCII
      digits, and halfwidth uppercase Latin letters where the citation
      contains them. Typographic variants converge to the canonical
      template.
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
      No sufficiently deterministic bn canonical rendering is
      declared for stock tickers or market-qualified symbols. Retain the
      source unchanged.
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
