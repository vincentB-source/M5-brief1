import os
import sys

sys.path.insert(0,
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                        ".."
                    )
                ))

from modules.calcul import calcul_du_carre

import pytest

def test_calcul_du_carre():  
    assert calcul_du_carre(12) == 144
    assert calcul_du_carre(-12) == 144