from collections import Counter


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        if not isinstance(skus, str):
            return -1

        if not all(ch.isalpha() for ch in skus):
            return -1

        prices = {
            'A': 50, 'B': 30,
            'C': 20, 'D': 15,
            'E': 40,'F': 10,
            'G': 20,'H': 10,
            'I': 35,'J': 60,
            'K': 70,'L': 90,
            'M': 15,'N': 40,
            'O': 10,'P': 50,
            'Q': 30,'R': 50,
            'S': 20,'T': 20,
            'U': 40,'V': 50,
            'W': 20,'X': 17,
            'Y': 20,'Z': 21,
        }
        offers = {
            'A': [(5, 200), (3, 130)],
            'B': [(2, 45)],
            'H': [(10, 80), (5, 45)],
            'K': [(2, 120)],
            'P': [(5, 200)],
            'Q': [(3, 80)],
            'V': [(3, 130), (2, 90)],


        }

        special_offers = {
            "E": {"buy_quantity": 2, "free_item": "B", "free_quantity": 1},
            "F": {"buy_quantity": 3, "free_item": "F", "free_quantity": 1},
            "N": {"buy_quantity": 3, "free_item": "M", "free_quantity": 1},
            'R': {'buy_quantity': 3, "free_item": "Q", "free_quantity": 1},
            'U': {'buy_quantity': 4, "free_item": "U", "free_quantity": 1},
        }

        group_offers = {

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
                for offer_quantity, offer_price in offers[item]:
                    num_offers = count // offer_quantity
                    total += num_offers * offer_price
                    count %= offer_quantity
            total += prices[item] * count

        return total


if __name__ == '__main__':
    market = CheckoutSolution()
    print(market.checkout("AAAAAAA"))
