from typing import NamedTuple
from collections import namedtuple
import pytest

class Money(NamedTuple):
    currency: str
    value: int

    def __eq__(self, another_money):
        if self.currency != another_money.currency:
            raise TypeError('Currency must be the same')
        return self.value == another_money.value


    def __add__(self, another_money):
        if self.currency != another_money.currency:
            raise TypeError('Currency must be the same')
        return self.value + another_money.value


    def __sub__(self, another_money):
        if self.currency != another_money.currency:
            raise TypeError('Currency must be the same')
        return self.value - another_money.value


    def __mul__(self, value: int):
        return self.value * value


Line = namedtuple('Line', ['sku', 'qty'])

def test_equality():
    assert Money('gbp', 10) == Money('gbp', 10)
    assert Line('RED-CHAIR', 5) == Line('RED-CHAIR', 5)


fiver = Money('gbp', 5)
tenner = Money('gbp', 10)


def test_can_add_money_values_for_the_same_currency():
    assert fiver + fiver == tenner


def test_can_subtract_money_values():
    assert tenner - fiver == fiver


def test_adding_different_currencies_fails():
    with pytest.raises(ValueError):
        Money('usd', 10) + Money('gbp', 10)


def test_can_multiply_money_by_a_number():
    assert fiver * 5 == Money('gbp', 25)


def test_multiplying_two_money_values_is_an_error():
    with pytest.raises(TypeError):
        tenner * fiver

