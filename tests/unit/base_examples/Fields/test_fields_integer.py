import pytest
from base_examples.Fields.models import IntegerModuloFieldElement


def test_init_normal():
    my_element = IntegerModuloFieldElement(1, 3)
    assert my_element.value == 1 and my_element.modulus == 3

def test_init_normalise():
    my_element = IntegerModuloFieldElement(10, 3)
    assert my_element.value == 1 and my_element.modulus == 3

def test_field_zero():
    my_element = IntegerModuloFieldElement(0, 1)
    assert my_element.zero() == 0

def test_field_one():
    my_element = IntegerModuloFieldElement(0, 1)
    assert my_element.one() == 1

def test_field_add_wrong():
    el1 = IntegerModuloFieldElement(1, 2)
    el2 = IntegerModuloFieldElement(1, 3)
    with pytest.raises(ValueError, match="Различные модули чисел"):
        el1 + el2

def test_field_add_right():
    el1 = IntegerModuloFieldElement(2, 10)
    el2 = IntegerModuloFieldElement(3, 10)
    res = (el1+el2)
    assert res.value == 5 and res.modulus == 10

def test_field_mul_wrong():
    el1 = IntegerModuloFieldElement(1, 2)
    el2 = IntegerModuloFieldElement(1, 3)
    with pytest.raises(ValueError, match="Различные модули чисел"):
        el1 * el2

def test_field_mul_right():
    el1 = IntegerModuloFieldElement(2, 10)
    el2 = IntegerModuloFieldElement(3, 10)
    res = (el1*el2)
    assert res.value == 6 and res.modulus == 10

def test_field_is_zero():
    el1 = IntegerModuloFieldElement(0, 3)
    assert el1.is_zero()
    el2 = IntegerModuloFieldElement(1, 3)
    el1 = el1 + el2
    assert el1.is_zero() is False

def test_field_eq():
    el1 = IntegerModuloFieldElement(2, 10)
    el2 = IntegerModuloFieldElement(3, 10)
    assert el1 != el2
