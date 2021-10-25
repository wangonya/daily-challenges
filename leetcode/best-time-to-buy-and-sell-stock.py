from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


s = Solution()
assert s.maxProfit([3,7,1,5,3,6,4]) == 5
assert s.maxProfit([7,6,4,3,1]) == 0
