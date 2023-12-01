"""Testing formula 3.23 of NEN-EN 1992-1-1+C2:2011."""
# pylint: disable=arguments-differ
import pytest

from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_3_materials.formula_3_23 import Form3Dot23FlexuralTensileStrength


class TestForm3Dot23TensileBendingStrength:
    """Validation for formula 3.23 from NEN-EN 1992-1-1+C2:2011."""

    def test_evaluation_1(self) -> None:
        """Test the evaluation of the result."""
        # Example values
        h = 305.3  # mm
        f_ctm = 23.8  # MPa

        form_3_23 = Form3Dot23FlexuralTensileStrength(h=h, f_ctm=f_ctm)

        # Expected result, manually calculated
        manually_calculated_result = 30.81386

        assert form_3_23 == pytest.approx(expected=manually_calculated_result, rel=1e-5)

    def test_evaluation_2(self) -> None:
        """Test the evaluation of the result."""
        # Example values
        h = 1000  # mm
        f_ctm = 23.8  # MPa

        form_3_23 = Form3Dot23FlexuralTensileStrength(h=h, f_ctm=f_ctm)

        # Expected result, manually calculated
        manually_calculated_result = 23.8

        assert form_3_23 == pytest.approx(expected=manually_calculated_result, rel=1e-4)

    def test_raise_error_when_negative_h_is_given(self) -> None:
        """Test a negative value for h."""
        # Example values
        h = -1000  # mm
        f_ctm = 23.8  # MPa

        with pytest.raises(ValueError):
            Form3Dot23FlexuralTensileStrength(h=h, f_ctm=f_ctm)

    def test_raise_error_when_negative_f_ctm_is_given(self) -> None:
        """Test a negative value for f_ctm."""
        # Example values
        h = 1000  # mm
        f_ctm = -23.8  # MPa

        with pytest.raises(ValueError):
            Form3Dot23FlexuralTensileStrength(h=h, f_ctm=f_ctm)
