#  file name test_*.py  *_test.py
# function
import pytest

from main import *

# -------------- negative check password test  --------------
def test_check_password1_N():
    password_to_test = 'Hothaifagfhjnhbg'
    assert not check_password(password_to_test)


def test_check_password2_N():
    password_to_test = 'othaifagf123123'
    expected = check_password(password_to_test)
    actual = False
    assert expected == actual


def test_check_password3_N():
    password_to_test = 'fagfasfasg'
    assert not check_password(password_to_test)


# -------------- negative check password test  --------------

# -------------- positive check password test  --------------

def test_check_password_P():
    password = 'Hothaifa12344'
    assert check_password(password)
# -------------- positive check password test  --------------
