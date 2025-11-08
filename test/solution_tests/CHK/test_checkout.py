import pytest
from lib.solutions.CHK.checkout_solution import CheckoutSolution


def test_checkout():
    market = CheckoutSolution()
    assert market.checkout("A") == 50

