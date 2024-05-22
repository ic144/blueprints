"""Formula 5.15 from NEN-EN 1992-1-1+C2:2011: Chapter 5 - Structural Analysis."""

import math

from blueprints.codes.eurocode.nen_en_1992_1_1_c2_2011 import NEN_EN_1992_1_1_C2_2011
from blueprints.codes.formula import Formula
from blueprints.codes.latex_formula import LatexFormula
from blueprints.type_alias import DIMENSIONLESS, M
from blueprints.validations import raise_if_negative


class Form5Dot15EffectiveLengthBraced(Formula):
    """Class representing formula 5.15 for the calculation of the slenderness ratio, :math:`λ`."""

    label = "5.15"
    source_document = NEN_EN_1992_1_1_C2_2011

    def __init__(self, k_1: DIMENSIONLESS, k_2: DIMENSIONLESS, height: M) -> None:
        """[:math:`l_{0}`] Effective length for braced members [:math:`-`].

        NEN-EN 1992-1-1+C2:2011 art.5.8.3.2(1) - Formula (5.15)

        Parameters
        ----------
        k_1 : -
            [:math:`k_{1}`] Relative flexibility of rotational constraint at end 1 [:math:`-`].
        k_2 : -
            [:math:`k_{1}`] Relative flexibility of rotational constraint at end 2 [:math:`-`].
        l : M
            [:math:`l`] Clear height of compression member between end restraints [:math:`M`].
        """
        super().__init__()
        self.k_1 = k_1
        self.k_2 = k_2
        self.height = height

    @staticmethod
    def _evaluate(
        k_1: DIMENSIONLESS,
        k_2: DIMENSIONLESS,
        height: M,
    ) -> DIMENSIONLESS:
        """Evaluates the formula, for more information see the __init__ method."""
        raise_if_negative(k_1=k_1, k_2=k_2, height=height)
        return 0.5 * height * math.sqrt((1 + k_1 / (0.45 + k_1)) * (1 + k_2 / (0.45 + k_2)))

    def latex(self) -> LatexFormula:
        """Returns LatexFormula object for formula 5.15."""
        return LatexFormula(
            return_symbol=r"l_0",
            result=f"{self:.3f}",
            equation=r"0.5 \cdot l \cdot \sqrt{(1+\frac{k_1}{0.45 \cdot k_1}) \cdot (1 + \frac{k_2}{0.45 \cdot k_2})}",
            numeric_equation=rf"0.5 \cdot {self.height:.3f} \cdot \sqrt{{(1+\frac{{{self.k_1:.3f}}}{{0.45 \cdot "
            rf"{self.k_1:.3f}}}) \cdot (1 + \frac{{{self.k_2:.3f}}}{{0.45 \cdot {self.k_2:.3f}}})}}",
            comparison_operator_label="=",
        )
