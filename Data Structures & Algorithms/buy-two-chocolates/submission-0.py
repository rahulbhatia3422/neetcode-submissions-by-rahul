from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Track the two cheapest prices
        cheapest, second_cheapest = float('inf'), float('inf')

        for price in prices:
            if price < cheapest:
                cheapest, second_cheapest = price, cheapest
            elif price < second_cheapest:
                second_cheapest = price

        total_cost = cheapest + second_cheapest

        # Return leftover if affordable, else original money
        if total_cost <= money:
            return money - total_cost
        return money
