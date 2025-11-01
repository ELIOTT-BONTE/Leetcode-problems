class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        minVal = prices[0]
        for i in range(len(prices)):
            minVal = min(minVal, prices[i])
            maxDiff = max(maxDiff, prices[i] - minVal)
        return maxDiff