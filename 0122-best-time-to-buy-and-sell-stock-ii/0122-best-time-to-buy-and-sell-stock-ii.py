class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0

        for i,p in enumerate(prices[:-1]):
            if p < prices[i+1]:
                profit += prices[i+1]-p

        return profit