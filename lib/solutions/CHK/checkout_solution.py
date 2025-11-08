from collections import Counter


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        if not isinstance(skus, str):
            return -1

        if not all(ch.isalpha() for ch in skus):
            return -1

        prices = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            'E': 40,
        }
        offers = {
            'A': (3, 130),
            'B': (2, 45),
        }

        special_offers = {
            "E": {"buy_quantity": 2, "free_item": "B", "free_quantity": 1},
        }

        for item in skus:
            if item not in prices:
                return -1

        counts = Counter(skus)

        # apply special offers
        for item, rule in special_offers.items():
            if item in counts:
                num_of_valid_offers = counts[item] // rule["buy_quantity"]
                free_item = rule["free_item"]
                if rule["free_item"] in counts:
                    # Deduct free items from count
                    counts[free_item] = max(0, counts[free_item] - num_of_valid_offers * rule["free_quantity"])


        total = 0
        for item, count in counts.items():
            if item in offers:
                offer_quantity, offer_price = offers[item]
                offer_groups = count // offer_quantity
                remainder = count % offer_quantity
                total += offer_groups * offer_price + remainder * prices[item]
            else:
                total += prices[item] * count

        return total


if __name__ == '__main__':
    market = CheckoutSolution()
    print(market.checkout("C"))





