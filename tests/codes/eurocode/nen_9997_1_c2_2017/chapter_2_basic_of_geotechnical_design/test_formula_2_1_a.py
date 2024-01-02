"""Module contains tests for formula 2.1a from NEN 9997-1+C2:2017: Chapter 2: Basis of geotechnical design."""
import pytest

from blueprints.codes.eurocode.nen_9997_1_c2_2017.chapter_2_basic_of_geotechnical_design.formula_2_1_a import Form2Dot1ADesignValueLoad
from blueprints.codes.eurocode.nen_9997_1_c2_2017.chapter_2_basic_of_geotechnical_design.formula_2_1_b import Form2Dot1BRepresentativeValue
from blueprints.type_alias import DIMENSIONLESS
from blueprints.validations import NegativeValueError


class TestForm2Dot1ADesignValueLoad:
    """Class containing tests for formula 2.1a from NEN 9997-1+C2:2017: Chapter 2: Basis of geotechnical design."""

    @pytest.mark.parametrize(
        ("gamma_f", "f_rep", "expected_result"),
        [
            (1.35, 100, 135),
            (1.35, 0.0, 0.0),
            (1.35, -100, -135),
            (-1.35, 1.0, None),
        ],
    )
    def test_formula_2_1_a(
        self,
        gamma_f: DIMENSIONLESS,
        f_rep: float,
        expected_result: float,
    ) -> None:
        """Method to test formula 2.1a from NEN 9997-1+C2:2017: Chapter 2: Basis of geotechnical design."""
        if expected_result is None:
            with pytest.raises(NegativeValueError):
                Form2Dot1ADesignValueLoad(gamma_f=gamma_f, f_rep=f_rep)
        else:
            assert Form2Dot1ADesignValueLoad(gamma_f=gamma_f, f_rep=f_rep) == pytest.approx(expected_result, rel=1e-9)

    def test_integration_with_2_1_b(self) -> None:
        """Test the integration of formula 2.1a with 2.1b."""
        f_rep = Form2Dot1BRepresentativeValue(psi=2, f_k=50)
        gamma_f = 1.35
        result = Form2Dot1ADesignValueLoad(gamma_f=gamma_f, f_rep=f_rep)

        assert result == pytest.approx(expected=135, rel=1e-9)
