from main import *
import pytest


class TestWithdraw:
    @pytest.mark.parametrize('amount', [4000, 4100, 5050, 330, 5555])
    def test_withdraw_N(self, amount):
        actual = withdraw(amount)
        expected = False
        assert actual == expected

    @pytest.mark.parametrize('amount', [3900, 100])
    def test_withdraw_P(self, amount):
        actual = withdraw(amount)
        expected = True
        assert actual == expected


class TestDeposit:
    @pytest.mark.parametrize('amount', [-100, 0, 11000])
    def test_deposit_n(self, amount):
        actual = deposit(amount)
        expected = False
        assert actual == expected

    @pytest.mark.parametrize('amount', [5000, 10000])
    def test_deposit_p(self, amount):
        actual = deposit(amount)
        expected = True
        assert actual == expected
