# ag2latin

Transliterate Ancient Greek text to Latin characters.

## Installation

```bash
git clone https://github.com/diyclassics/ag2latin.git
cd ag2latin
pip install -e .
```

## Usage

### Command Line

```bash
# Transliterate a word
ag2latin "μῆνιν"
# μῆνιν -> MĒNIN

# Run examples
ag2latin
# μῆνιν -> MĒNIN
# θεὰ -> THEA
# ...
```

### Python

```python
from ag2latin import ag2latin

ag2latin("μῆνιν")      # 'MĒNIN'
ag2latin("θεὰ")        # 'THEA'
ag2latin("ἑλώρια")     # 'HELŌRIA'
ag2latin("ῥίγος")      # 'RHIGOS'
```

## Features

- Handles breathing marks (rough → H, smooth → removed)
- Converts η/ω to Ē/Ō (macrons for long vowels)
- Processes digraphs: θ→TH, φ→PH, χ→CH, ψ→PS
- Gamma nasals: γγ→NG, γκ→NK, γχ→NCH, γξ→NX
- Preserves iota subscript: ῃ→ĒI, ῳ→ŌI, ᾳ→AI
- Double rho: ῤῥ→RRH (e.g., Πύῤῥος→PYRRHOS)
- Upsilon → Y (traditional Latin convention)
- Supports multi-word input with punctuation
- Normalizes Unicode (NFD decomposition)

**Note on uppercase:** Output is uppercase. This follows the observation in Feeney 2016 p. 39 that Greek and Latin appear strikingly similar in uppercase letterforms.

## Development

```bash
# Run tests
pytest

# Lint
ruff check .
```

## Known Limitations

- Circumflex on α/ι/υ does not add macron (ᾷ→AI not ĀI)
- No handling of archaic letters (digamma, koppa, sampi)

## Changelog

### v0.2.1
- Add gamma nasal rule: γγ→NG, γκ→NK, γχ→NCH, γξ→NX
- Add iota subscript preservation: ῃ→ĒI, ῳ→ŌI, ᾳ→AI
- Fix double rho: Πύῤῥος→PYRRHOS (not PYRHROS)
- Fix rho breathing at word boundaries (not just string start)
- Change υ→Y (was U) for Latin convention
- Expand test suite to 37 tests

### v0.2.0
- Fix duplicate dictionary keys causing incorrect mappings for Ή, ῌ
- Fix character mappings: Ὼ, Ώ, Ὴ now correctly map to Ō/Ē (not ŌI/ĒI)
- Fix rough breathing handling for words mid-string
- Add test suite (27 tests)
- Add ruff linting and pytest configuration

### v0.1.0
- Initial release

## License

MIT License - see [LICENSE](LICENSE)

## Works cited

- Feeney, D. 2016. *Beyond Greek: The Beginnings of Latin Literature*. Cambridge, MA: Harvard University Press.

## Author

Patrick J. Burns (patrick@diyclassics.org)
