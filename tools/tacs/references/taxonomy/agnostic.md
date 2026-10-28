# Language-agnostic taxonomy and category methodology

These phenomenon definitions are shared across supported languages, although their applicability and realizations may differ. The Description column reproduces the released ETC-Bench definition; Recognition guidance helps recover the semantic value and select the complete span. Neither column defines a canonical output form.

## Numeric expressions

Methodology: recover the structured numeric value and its semantic role. A specialized role takes precedence over `cardinal`. Rendering requires an exact `C(language, category, phenomenon)` contract in the language reference.

| Phenomenon | Description | Recognition guidance |
|---|---|---|
| cardinal | A number written with digits that is read aloud as words (e.g. '45' vs. 'forty-five'). | A quantity; distinguish it from identifiers and specialized formats. |
| ordinal | A number written with digits or a suffix that is read aloud as an ordinal (e.g. '3rd' vs. 'third'). | Rank or ordered position, including its ordinal marker. |
| decimal | A decimal written with digits and a point that is read aloud as words (e.g. '3.14' vs. 'three point one four'). | Integral and fractional parts with stated precision. |
| fraction | A fraction written with a slash or hyphen that is read aloud as words (e.g. '1/2' vs. 'one half'). | Numerator, denominator, and any mixed-number component. |
| date | A date written in numeric form that is read aloud as words (e.g. '2024/05/03' vs. 'May third, 2024'). | Complete date expression; resolve language-specific field order from context. |
| time | A time written with digits and separators that is read aloud as words (e.g. '5:30' vs. 'five thirty'). | Complete clock time, including period or timezone when present. |
| currency | A money amount written with a symbol and digits that is read aloud as words (e.g. '$5' vs. 'five dollars'). | Amount plus currency identity; treat as one semantic object. |
| unit | A quantity written with a number and a unit abbreviation that is read aloud in full (e.g. '10 km' vs. 'ten kilometers'). | Quantity plus measurement unit and necessary grammatical number. |
| phone | A phone number written with digits and separators that is read aloud digit by digit (e.g. '(555) 123-4567'). | Complete telephone identifier; preserve every digit and grouping role. |
| roman | A number written as a Roman numeral that is read aloud as words (e.g. 'IV' vs. 'four'). | Roman numeral only when context establishes numeric use. |
| sports_score | A sports score written with digits and a dash that is read aloud as words (e.g. '3-2' vs. 'three to two'). | Ordered competitors' scores; do not reinterpret as subtraction or range. |

## Symbols and markers

Methodology: recover the complete structured expression, including ordered letters, digits, signs, separators, and named entities that contribute meaning. Rendering requires an exact `C(language, category, phenomenon)` contract.

| Phenomenon | Description | Recognition guidance |
|---|---|---|
| address | An address written with abbreviations and numbers that is read aloud in full (e.g. '123 Main St' vs. '123 Main Street'). | Complete postal/street address component under normalization. |
| isbn | An ISBN written as a code that is read aloud digit by digit (e.g. '978-0-306-40615-7'). | Complete ISBN identifier, preserving every digit and check character. |
| biological | A biological classification written as a code that is read aloud as a name (e.g. 'E. coli' vs. 'Escherichia coli'). | Scientific biological name/notation as a unit. |
| chemical | A chemical formula written with symbols and subscripts that is read aloud as a name (e.g. 'H2O' vs. 'water'). | Chemical formula, including element identity and subscripts/counts. |
| legal | A legal reference written with abbreviations that is read aloud in full (e.g. 'U.S.C.' vs. 'United States Code'). | Legal citation with all section/article identifiers. |
| vehicle | A vehicle or product code written with letters and digits that is read aloud as a code (e.g. 'BMW X5'). | Vehicle or product code; preserve ordered alphanumeric identity. |
| coordinates | Geographic coordinates written with degrees and symbols that are read aloud as words (e.g. '40.7°N 74.0°W'). | Coordinate pair/value including direction, degree and subdivisions. |
| version | A version number written with digits and dots that is read aloud as words or digits (e.g. 'v2.1'). | Version identifier; preserve component boundaries and order. |
| license | A license plate or serial number written with mixed characters that is read aloud character by character. | License plate or serial identifier, read as an identifier. |
| musical | Musical notation written as symbols that is read aloud as words (e.g. 'C♯' vs. 'C sharp'). | Musical notation whose conventional spoken form is recoverable. |
| stock | A stock ticker written as letters that is read aloud as letters (e.g. 'AAPL'). | Stock ticker or market-qualified symbol, not an ordinary word. |
| url | A URL or email address written with dots and slashes that is read aloud as words or letters (e.g. 'example.com'). | URL or email; preserve the complete address and meaningful separators. |
| hashtag | A hashtag or mention written with symbols that is read aloud as words (e.g. '#topic' vs. 'hashtag topic'). | Hashtag or mention, including the marker's conventional reading. |
| math | A mathematical expression written with symbols that is read aloud as words (e.g. 'a² + b²' vs. 'a squared plus b squared'). | Complete mathematical expression; preserve operators and grouping. |

## Language-specific category methodology

The language reference supplies the closed phenomenon list.

- `abbreviations`: recover the contextually intended expansion and grammatical realization. Ambiguity means no edit; recovery alone does not authorize expansion.
- `orthographic_variants`: recover the shared lexical or character identity and equivalence group. Do not choose a target without an exact contract.
- `homophonic_substitutions`: require an inventory-defined equivalence relation and applicability condition. Do not collapse arbitrary homophones; a contract must declare the representative surface.

For every category, absence of an exact applicable contract means retaining the source span.
