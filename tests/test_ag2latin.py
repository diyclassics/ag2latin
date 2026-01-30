"""Tests for ag2latin transliteration."""

from ag2latin import ag2latin


class TestDocstringExamples:
    """Test cases from the function docstrings."""

    def test_menin(self):
        assert ag2latin("μῆνιν") == "MĒNIN"

    def test_thea(self):
        assert ag2latin("θεὰ") == "THEA"

    def test_heloria(self):
        assert ag2latin("ἑλώρια") == "HELŌRIA"

    def test_peleiadeo(self):
        # Note: Alpha with acute becomes plain A (acute marks stress, not length)
        assert ag2latin("Πηληϊάδεω") == "PĒLĒIADEŌ"

    def test_rhigos(self):
        assert ag2latin("ῥίγος") == "RHIGOS"


class TestBreathingMarks:
    """Test handling of rough and smooth breathing marks."""

    def test_rough_breathing_becomes_h(self):
        # ἑ (epsilon with rough breathing) -> HE
        assert ag2latin("ἑ") == "HE"

    def test_smooth_breathing_removed(self):
        # ἀ (alpha with smooth breathing) -> A
        assert ag2latin("ἀ") == "A"

    def test_rough_breathing_on_rho(self):
        # ῥ (rho with rough breathing) -> RH
        assert ag2latin("ῥ") == "RH"

    def test_rough_breathing_word_initial(self):
        # Rough breathing at start of word
        assert ag2latin("ἅ") == "HA"

    def test_rough_breathing_mid_string(self):
        # Rough breathing on word that's not at string start
        assert ag2latin("test ἑλώρια") == "TEST HELŌRIA"

    def test_multiple_rough_breathings(self):
        # Multiple words with rough breathing
        assert ag2latin("ἑλώρια ἅμα") == "HELŌRIA HAMA"


class TestCapitalization:
    """Test handling of capital Greek letters."""

    def test_capital_alpha(self):
        assert ag2latin("Α") == "A"

    def test_capital_word(self):
        # Capital letter at start (υ -> Y)
        assert ag2latin("Ἀχιλλεύς") == "ACHILLEYS"

    def test_all_caps_input(self):
        # All uppercase Greek
        assert ag2latin("ΜΗΝΙΝ") == "MĒNIN"


class TestMultiWordInput:
    """Test sentences and phrases with multiple words."""

    def test_two_words(self):
        result = ag2latin("μῆνιν ἄειδε")
        assert result == "MĒNIN AEIDE"

    def test_phrase_with_punctuation(self):
        result = ag2latin("μῆνιν ἄειδε, θεά")
        assert result == "MĒNIN AEIDE, THEA"


class TestSpecialCharacters:
    """Test digraphs and special Greek characters."""

    def test_theta(self):
        assert ag2latin("θ") == "TH"

    def test_phi(self):
        assert ag2latin("φ") == "PH"

    def test_chi(self):
        assert ag2latin("χ") == "CH"

    def test_psi(self):
        assert ag2latin("ψ") == "PS"

    def test_xi(self):
        assert ag2latin("ξ") == "X"


class TestLongVowels:
    """Test eta and omega produce macrons."""

    def test_eta(self):
        assert ag2latin("η") == "Ē"

    def test_omega(self):
        assert ag2latin("ω") == "Ō"


class TestGammaNasals:
    """Test gamma before velars becomes nasal (n)."""

    def test_double_gamma(self):
        # ἄγγελος -> ANGELOS (not AGGELOS)
        assert ag2latin("ἄγγελος") == "ANGELOS"

    def test_gamma_kappa(self):
        # ἄγκυρα -> ANKYRA (υ -> Y)
        assert ag2latin("ἄγκυρα") == "ANKYRA"

    def test_gamma_chi(self):
        # ἄγχω -> ANCHŌ
        assert ag2latin("ἄγχω") == "ANCHŌ"

    def test_gamma_xi(self):
        # σφίγξ -> SPHINX (γξ -> NX, ξ already includes the "ks" sound)
        assert ag2latin("σφίγξ") == "SPHINX"


class TestRhoBreathing:
    """Test rho with rough breathing in various positions."""

    def test_rho_word_initial(self):
        assert ag2latin("ῥίγος") == "RHIGOS"

    def test_rho_mid_sentence(self):
        # Rho with breathing mid-string should still be RH
        assert ag2latin("καὶ ῥίγος") == "KAI RHIGOS"

    def test_double_rho(self):
        # Πύῤῥος -> PYRRHOS
        assert ag2latin("Πύῤῥος") == "PYRRHOS"


class TestIotaSubscript:
    """Test iota subscript is preserved."""

    def test_eta_iota_subscript(self):
        # τῇ -> TĒI
        assert ag2latin("τῇ") == "TĒI"

    def test_omega_iota_subscript(self):
        # ᾠδή -> ŌIDĒ
        assert ag2latin("ᾠδή") == "ŌIDĒ"

    def test_alpha_iota_subscript(self):
        # ᾳ (alpha + iota subscript) -> AI
        # Note: circumflex on alpha (ᾷ) doesn't add macron - known limitation
        assert ag2latin("ᾳ") == "AI"


class TestEdgeCases:
    """Edge cases and potential issues."""

    def test_empty_string(self):
        assert ag2latin("") == ""

    def test_single_character(self):
        assert ag2latin("α") == "A"

    def test_latin_passthrough(self):
        # If given Latin text, should pass through unchanged (after upper)
        result = ag2latin("hello")
        assert result == "HELLO"

    def test_mixed_greek_latin(self):
        # Mixed input - Greek gets transliterated, Latin stays
        result = ag2latin("test μῆνιν")
        assert result == "TEST MĒNIN"
