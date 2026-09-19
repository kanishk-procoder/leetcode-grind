class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float("inf")
        profit = 0
        max_profit = 0

        for i in range(0,len(prices)) :
            minimum = min(minimum, prices[i])
            profit = prices[i] - minimum
            max_profit = max(profit, max_profit)

        return max_profit