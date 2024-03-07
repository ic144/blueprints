"""Testing test formula for 3.28, 3.29 and 3.30 of NEN-EN 1992-1-1+C2:2011."""

import pytest

from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_3_materials.sub_formula_3_28_29_30 import SubForm3Dot282930Mu


class TestSubForm3Dot282930Mu:
    """Validation for formula for 3.28, 3.29 and 3.30 from NEN-EN 1992-1-1+C2:2011."""

    def test_evaluation(self) -> None:
        """Test the evaluation of the result."""
        # Example values
        sigma_pi = 2.4  # MPa
        f_pk = 8.5  # MPa

        sub_form_3_28_29_30 = SubForm3Dot282930Mu(sigma_pi=sigma_pi, f_pk=f_pk)

        # Expected result, manually calculated
        manually_calculated_result = 0.282353

        assert sub_form_3_28_29_30 == pytest.approx(expected=manually_calculated_result, rel=1e-4)

    def test_raise_error_when_negative_f_pk_is_given(self) -> None:
        """Test a negative value."""
        # Example values
        sigma_pi = 2.4  # MPa
        f_pk = -8.5  # MPa

        with pytest.raises(ValueError):
            SubForm3Dot282930Mu(sigma_pi=sigma_pi, f_pk=f_pk)
