class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            curr_price = prices[i]
            max_profit = max(max_profit, curr_price - lowest_price)
            lowest_price = min(lowest_price, curr_price)
        return max_profit