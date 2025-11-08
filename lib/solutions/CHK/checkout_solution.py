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

        counts = dict()
        for item in skus:
            counts[item] = counts.get(item, 0) + 1

        total = 0
        for item, count in counts.items():
            if item in offers:
                offer_quantity, offer_price = offers[item]
                offer_groups = count // offer_quantity
                remainder = count % offer_quantity
                total += offer_groups*offer_price + remainder*prices[item]
            else:
                total += offers[item] * count

        return total

if __name__ == '__main__':
    market = CheckoutSolution()
    print(market.checkout(""))

