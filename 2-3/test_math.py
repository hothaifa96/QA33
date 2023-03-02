# pytest work only with files named :
#
#     test_*.py  -> test_square.py
#     *_test.py  -> test_math.py
import pytest


def test_1():
    actual = 2 + 8
    expected = 10

    assert actual == expected


def test_2():
    actual = 380 + 18400
    expected = 2000
    assert actual == expected


def test_3():
    actual = 5000
    limit = 0
    assert actual >= limit

@pytest.fixture
def balance():
    balance=2000
    return balance

def test_deposite_P(balance):
    amount = 5000
    expected = 7000
    assert expected == amount + balance


def test_withdraw_P(balance):
    amount = 1000
    expected = 1000
    assert expected == amount - balance
