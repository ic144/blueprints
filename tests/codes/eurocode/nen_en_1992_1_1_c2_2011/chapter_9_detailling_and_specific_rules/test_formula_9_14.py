"""Testing formula 9.14 of NEN-EN 1992-1-1+C2:2011."""

import pytest

from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_9_detailling_and_specific_rules.formula_9_14 import (
    Form9Dot14SplittingForceColumnOnRock,
)
from blueprints.validations import NegativeValueError


class TestForm9Dot14SplittingForceColumnOnRock:
    """Validation for formula 9.14 from NEN-EN 1992-1-1+C2:2011."""

    def test_evaluation(self) -> None:
        """Test the evaluation of the result."""
        # Example values
        c = 50  # mm
        h = 100  # mm
        n_ed = 200  # kN
        form_9_14 = Form9Dot14SplittingForceColumnOnRock(c=c, h=h, n_ed=n_ed)

        # Expected result, manually calculated
        manually_calculated_result = 25

        assert form_9_14 == pytest.approx(expected=manually_calculated_result, rel=1e-4)

    def test_raise_error_when_negative_c_is_given(self) -> None:
        """Test the evaluation of the result."""
        c = -50  # mm
        h = 100  # mm
        n_ed = 200  # kN

        with pytest.raises(NegativeValueError):
            Form9Dot14SplittingForceColumnOnRock(c=c, h=h, n_ed=n_ed)

    def test_raise_error_when_negative_h_is_given(self) -> None:
        """Test the evaluation of the result."""
        c = 50  # mm
        h = -100  # mm
        n_ed = 200  # kN

        with pytest.raises(NegativeValueError):
            Form9Dot14SplittingForceColumnOnRock(c=c, h=h, n_ed=n_ed)

    def test_raise_error_when_negative_n_ed_is_given(self) -> None:
        """Test the evaluation of the result."""
        c = 50  # mm
        h = 100  # mm
        n_ed = -200  # kN

        with pytest.raises(NegativeValueError):
            Form9Dot14SplittingForceColumnOnRock(c=c, h=h, n_ed=n_ed)

    @pytest.mark.parametrize(
        ("representation", "expected"),
        [
            (
                "complete",
                r"F_s = 0.25 \cdot ( 1 - c / h ) \cdot N_{Ed} = 0.25 \cdot ( 1 - 50.000 / 100.000 ) \cdot 200.000 = 25.000",
            ),
            ("short", r"F_s = 25.000"),
        ],
    )
    def test_latex(self, representation: str, expected: str) -> None:
        """Test the latex representation of the formula."""
        # Example values
        c = 50  # mm
        h = 100  # mm
        n_ed = 200  # kN

        # Object to test
        form_9_14_latex = Form9Dot14SplittingForceColumnOnRock(c=c, h=h, n_ed=n_ed).latex()

        actual = {"complete": form_9_14_latex.complete, "short": form_9_14_latex.short}

        assert actual[representation] == expected, f"{representation} representation failed."
