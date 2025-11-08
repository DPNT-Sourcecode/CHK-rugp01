import pytest
from lib.solutions.CHK.checkout_solution import CheckoutSolution


def test_checkout():
    market = CheckoutSolution()
    assert market.checkout("A") == 50

class TestCheckout:
    def test_single_items(self):
        market = CheckoutSolution()
        assert market.checkout("A") == 50
        assert market.checkout("B") == 30
        assert market.checkout("C") == 20
        assert market.checkout("D") == 15
        assert market.checkout("E") == 40

    def test_mixed_items(self):
        market = CheckoutSolution()
        assert market.checkout("ABCDABA") == 210

    def test_invalid_items(self):
        market = CheckoutSolution()
        assert market.checkout(float) == -1
        assert market.checkout(123) == -1
        assert market.checkout(["A", "B"]) == -1



