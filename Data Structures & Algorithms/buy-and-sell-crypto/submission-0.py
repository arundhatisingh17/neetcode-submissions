class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minCurr = float('inf')
        maxProfit = 0
        
        for i in range(len(prices)):
            minCurr = min(minCurr, prices[i])
            maxProfit = max(maxProfit, prices[i] - minCurr)

        return maxProfit