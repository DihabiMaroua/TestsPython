import pytest
from math_functions import division

def test_division_positive():
    assert division(10, 2) == 5

def test_division_negative():
    assert division(-10, 2) == -5

def test_division_zero():
    with pytest.raises(ValueError):
        division(10, 0)
