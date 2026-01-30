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
- Supports multi-word input with punctuation
- Normalizes Unicode (NFD decomposition)

## Development

```bash
# Run tests
pytest

# Lint
ruff check .
```

## Changelog

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

## Author

Patrick J. Burns (patrick@diyclassics.org)
