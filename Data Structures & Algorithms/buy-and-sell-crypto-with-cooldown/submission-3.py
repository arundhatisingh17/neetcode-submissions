class Solution:
    def recurBuilder(self, prices: List[int], idx: int, maxProfit: int, holding: bool, seen: dict) -> int:

        if idx >= len(prices):
            return maxProfit

        key = (idx, maxProfit, holding)
        if key in seen:
            return maxProfit

        sell = 0
        buy = 0

        if not holding:
            buy = self.recurBuilder(prices, idx + 1, maxProfit - prices[idx], True, seen)

        if holding:
            sell = self.recurBuilder(prices, idx + 2, maxProfit + prices[idx], False, seen)

        nothing = self.recurBuilder(prices, idx + 1, maxProfit, holding, seen)

        maxProfit = max(buy, sell, nothing)
        seen[key] = maxProfit

        return maxProfit

    def maxProfit(self, prices: List[int]) -> int:
        
        # there are two paths you need to take over here - you either buy and retain or you sell and move on
        # define separate recursive paths for each of these options
        holding = False
        seen = {}

        return self.recurBuilder(prices, 0, 0, holding, seen)
