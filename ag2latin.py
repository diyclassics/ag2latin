"""
ag2latin.py

Transliterate Ancient Greek text to Latin.

Author: Patrick J. Burns (patrick@diyclassics.org)
License: MIT
Date: 2023-10-05
"""

import argparse
import re
import unicodedata


def ag2latin(text: str) -> str:
    """
    Transliterate Ancient Greek text to Latin.

    Args:
        text (str): The Ancient Greek text to be transliterated.

    Returns:
        str: The transliterated Latin text.

    Examples:
        >>> ag2latin("μῆνιν")
        'MĒNIN'

        >>> ag2latin("θεὰ")
        'THEA'

        >>> ag2latin("ἑλώρια")
        'HELŌRIA'

        >>> ag2latin("Πηληϊάδεω")
        'PĒLĒIADEŌ'

        >>> ag2latin("ῥίγος")
        'RHIGOS'
    """
    # Normalize the text to decompose characters with diacritics
    text = unicodedata.normalize("NFD", text)

    # Handle breathing marks and remove other diacritical marks in a single pass
    result = []
    for char in text:
        if char == "\u0314":  # Rough breathing (U+0314)
            # Insert H before the preceding letter (breathing follows its letter in NFD)
            if result:
                preceding = result.pop()
                result.append("H")
                result.append(preceding)
            else:
                result.append("H")
        elif char == "\u0345":  # Combining Greek Ypogegrammeni (iota subscript)
            result.append("I")
        elif char == "\u0313" or unicodedata.category(char) == "Mn":
            # Smooth breathing (U+0313) or other diacritical marks - skip
            continue
        else:
            result.append(char)

    text = "".join(result)

    # Convert text to uppercase
    text = text.upper()

    # Dictionary mapping Greek characters to Latin characters
    greek_to_latin = {
        "Α": "A",
        "Β": "B",
        "Γ": "G",
        "Δ": "D",
        "Ε": "E",
        "Ζ": "Z",
        "Η": "Ē",
        "Θ": "TH",
        "Ι": "I",
        "Ϊ": "I",
        "Κ": "K",
        "Λ": "L",
        "Μ": "M",
        "Ν": "N",
        "Ξ": "X",
        "Ο": "O",
        "Π": "P",
        "Ρ": "R",
        "Σ": "S",
        "Τ": "T",
        "Υ": "Y",
        "Ϋ": "Y",
        "Φ": "PH",
        "Χ": "CH",
        "Ψ": "PS",
        "Ω": "Ō",
        "ᾼ": "Ā",
        "Ί": "Ī",
        "Ῡ": "Ū",
        "Ή": "Ē",
        "ῌ": "ĒI",
        "ῼ": "ŌI",
        "Ὼ": "Ō",
        "Ώ": "Ō",
        "Ὴ": "Ē",
    }

    # Create translation table
    translation_table = str.maketrans(greek_to_latin)

    # Transliterate the text
    transliterated_text = text.translate(translation_table)

    # Apply gamma nasal rule: γ before γ,κ,χ,ξ is pronounced /n/
    transliterated_text = transliterated_text.replace("GG", "NG")
    transliterated_text = transliterated_text.replace("GK", "NK")
    transliterated_text = transliterated_text.replace("GCH", "NCH")
    transliterated_text = transliterated_text.replace("GX", "NX")

    # Fix double rho: ῤῥ → RRH (H goes at end, not middle)
    transliterated_text = transliterated_text.replace("RHR", "RRH")

    # Fix rho with rough breathing at word boundaries: HR → RH
    transliterated_text = re.sub(r"(^|(?<=\s))HR", r"\1RH", transliterated_text)

    return transliterated_text


def main():
    parser = argparse.ArgumentParser(
        description="Transliterate Ancient Greek text to Latin."
    )
    parser.add_argument(
        "text",
        type=str,
        nargs="?",
        help="The Ancient Greek text to be transliterated.",
    )
    args = parser.parse_args()

    if args.text:
        # Transliterate the provided Greek text
        latin_text = ag2latin(args.text)
        print(f"{args.text} -> {latin_text}")
    else:
        # List of example Greek texts
        examples: list[str] = [
            "μῆνιν",
            "θεὰ",
            "Αχιλῆος",
            "ἄειδε",
            "ἑλώρια",
            "Πηληϊάδεω",
            "ῥίγος",
        ]

        # Loop over the examples and print the transliterated text
        for greek_text in examples:
            latin_text = ag2latin(greek_text)
            print(f"{greek_text} -> {latin_text}")


if __name__ == "__main__":
    main()
