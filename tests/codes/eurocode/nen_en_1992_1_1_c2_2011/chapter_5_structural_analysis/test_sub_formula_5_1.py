"""Testing sub-formulas for 5.1 of NEN-EN 1992-1-1+C2:2011."""
# pylint: disable=arguments-differ
import pytest

from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_5_structural_analysis.formula_5_1 import (
    SubForm5Dot1ReductionFactorLengthOrHeight,
    SubForm5Dot1ReductionFactorNumberOfMembers,
)


class TestSubForm5Dot1ReductionFactorLengthOrHeight:
    """Validation for sub-formula (αh) for 5.1 from NEN-EN 1992-1-1+C2:2011."""

    def test_evaluation(self) -> None:
        """Test the evaluation of the result."""
        # Example values
        l = 8  # m

        # Object to test
        sub_form_5_1 = SubForm5Dot1ReductionFactorLengthOrHeight(l=l)

        # Expected result, manually calculated
        manually_calculated_result = 0.7071

        assert sub_form_5_1 == pytest.approx(expected=manually_calculated_result, rel=1e-4)

    def test_raise_error_when_negative_l_is_given(self) -> None:
        """Test a negative value."""
        # Example values
        l = -3.5

        with pytest.raises(ValueError):
            SubForm5Dot1ReductionFactorLengthOrHeight(l=l)

    def test_raise_error_when_l_is_zero(self) -> None:
        """Test a zero value."""
        # Example values
        l = 0

        with pytest.raises(ValueError):
            SubForm5Dot1ReductionFactorLengthOrHeight(l=l)

    def test_alpha_h_is_between_two_thirds_when_l_is_high(self) -> None:
        """Test if the result is 2/3 when l is high."""
        # Example values
        l = 100  # m

        # Object to test
        sub_form_5_1 = SubForm5Dot1ReductionFactorLengthOrHeight(l=l)

        assert sub_form_5_1 == pytest.approx(expected=2 / 3, rel=1e-4)

    def test_alpha_h_is_one_when_l_is_low(self) -> None:
        """Test if the result is 1 when l is low."""
        # Example values
        l = 0.1

        # Object to test
        sub_form_5_1 = SubForm5Dot1ReductionFactorLengthOrHeight(l=l)

        assert sub_form_5_1 == pytest.approx(expected=1, rel=1e-4)


class TestSubForm5Dot1ReductionFactorNumberOfMembers:
    """Validation for sub-formula (αm) for 5.1 from NEN-EN 1992-1-1+C2:2011."""

    def test_evaluation(self) -> None:
        """Test the evaluation of the result."""
        # Example values
        m = 5

        # Object to test
        sub_form_5_1 = SubForm5Dot1ReductionFactorNumberOfMembers(m=m)

        # Expected result, manually calculated
        manually_calculated_result = 0.774596

        assert sub_form_5_1 == pytest.approx(expected=manually_calculated_result, rel=1e-4)

    def test_raise_error_when_negative_m_is_given(self) -> None:
        """Test a negative value."""
        # Example values
        m = -5

        with pytest.raises(ValueError):
            SubForm5Dot1ReductionFactorNumberOfMembers(m=m)

    def test_raise_error_when_m_is_zero(self) -> None:
        """Test a zero value."""
        # Example values
        m = 0

        with pytest.raises(ValueError):
            SubForm5Dot1ReductionFactorNumberOfMembers(m=m)
