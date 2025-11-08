class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        # Rules
        # A = 50, 3A = 130
        # B = 30, 2B = 45
        # C = 20, D = 15

        if not all(ch.isalpha() for ch in skus):
            return -1

        prices = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15
        }
        offers = {
            'A':(3,130),
            'B':(2,45),
        }

        for item in skus:
            if item not in prices:
                return -1

        



