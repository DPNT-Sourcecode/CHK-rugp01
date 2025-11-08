import pytest
from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout:
    def test_single_items(self):
        market = CheckoutSolution()
        assert market.checkout("A") == 50
        assert market.checkout("B") == 30
        assert market.checkout("C") == 20
        assert market.checkout("D") == 15
        assert market.checkout("E") == 40
        assert market.checkout("F") == 10

    def test_mixed_item_offers(self):
        market = CheckoutSolution()
        assert market.checkout("ABCDABA") == 210
        assert market.checkout("AAAAA") == 200
        assert market.checkout("AAAAAA") == 250
        assert market.checkout("AAAAAAAA") == 330

    def test_invalid_items(self):
        market = CheckoutSolution()
        assert market.checkout(float) == -1
        assert market.checkout(123) == -1
        assert market.checkout("B11A") == -1
        assert market.checkout(["A", "B"]) == -1

    def test_E_offer(self):
        market = CheckoutSolution()
        assert market.checkout("EEB") == 80
        assert market.checkout("EEBB") == 110

    def test_F_offer(self):
        market = CheckoutSolution()
        assert market.checkout("FFF") == 20
        assert market.checkout("FF") == 20
        assert market.checkout("FFFFFF") == 40
        assert market.checkout("FFFFFFF") == 50

    def test_H_offer(self):
        market = CheckoutSolution()
        assert market.checkout("HHHHH") == 45
        assert market.checkout("HHHHHHHHHH") == 80
        assert market.checkout("HHHHHHHHHHH") == 90

    def test_K_offer(self):
        market = CheckoutSolution()
        assert market.checkout("KK") == 150
        assert market.checkout("KKK") == 230

    def test_N_offer(self):
        market = CheckoutSolution()
        assert market.checkout("NNNM") == 120
        assert market.checkout("NNNMM") == 135

    def test_R_offer(self):
        market = CheckoutSolution()
        assert market.checkout("RRRQ") == 150
        assert market.checkout("RRRQQ") == 180

    def test_U_offer(self):
        market = CheckoutSolution()
        assert market.checkout("UUU") == 120
        assert market.checkout("UUUU") == 120
        assert market.checkout("UUUUU") == 160

    def test_V_offers(self):
        market = CheckoutSolution()
        assert market.checkout("VV") == 90
        assert market.checkout("VVV") == 130
        assert market.checkout("VVVVV") == 220




