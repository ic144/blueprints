"""Testing formula 8.12 of NEN-EN 1992-1-1+C2:2011."""

import pytest

from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011.chapter_8_detailing_of_reinforcement_and_prestressing_tendons.formula_8_12 import (
    Form8Dot12AdditionalShearReinforcement,
)
from blueprints.validations import NegativeValueError


class TestForm8Dot12AdditionalShearReinforcement:
    """Validation for formula 8.12 from NEN-EN 1992-1-1+C2:2011."""

    def test_evaluation(self) -> None:
        """Test the evaluation of the result."""
        # example values
        a_s = 100  # mm²
        n_1 = 2  # -
        form_8_12 = Form8Dot12AdditionalShearReinforcement(a_s=a_s, n_1=n_1)

        manually_calculated_result = 50  # mm²

        assert form_8_12 == pytest.approx(expected=manually_calculated_result, rel=1e-4)

    def test_raise_error_negative_a_s(self) -> None:
        """Test that an error is raised when a_s is negative."""
        # example values
        a_s = -100  # mm²
        n_1 = 2  # -

        with pytest.raises(NegativeValueError):
            Form8Dot12AdditionalShearReinforcement(a_s=a_s, n_1=n_1)

    def test_raise_error_negative_n_1(self) -> None:
        """Test that an error is raised when n_1 is negative."""
        # example values
        a_s = 100  # mm²
        n_1 = -2  # -

        with pytest.raises(NegativeValueError):
            Form8Dot12AdditionalShearReinforcement(a_s=a_s, n_1=n_1)
