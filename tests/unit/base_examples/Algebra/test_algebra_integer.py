import pytest
from base_examples.Algebra.models import IntegerAlgebra


def test_algebra_zero():
    algebra = IntegerAlgebra()
    assert algebra.zero() == 0

def test_algebra_one():
    algebra = IntegerAlgebra()
    assert algebra.one() == 1

def test_algebra_add():
    algebra = IntegerAlgebra()
    assert algebra.add(2, 3) == 5

def test_algebra_multiply():
    algebra = IntegerAlgebra()
    assert algebra.multiply(2, 3) == 6

def test_algebra_inverse_add():
    algebra = IntegerAlgebra()
    assert algebra.inverse_add(2) == -2

def test_inverse_multiply_positive():
    algebra = IntegerAlgebra()
    assert algebra.inverse_multiply(5) == 0.2

def test_inverse_multiply_zero():
    algebra = IntegerAlgebra()
    with pytest.raises(ZeroDivisionError, match="Деление на ноль"):
        algebra.inverse_multiply(0)

def test_inverse_multiply_negative():
    algebra = IntegerAlgebra()
    assert algebra.inverse_multiply(-2) == -0.5
