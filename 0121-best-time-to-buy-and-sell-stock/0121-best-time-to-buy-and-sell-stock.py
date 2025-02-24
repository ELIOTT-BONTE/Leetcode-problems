class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxDiff = 0
        mini = float("inf")
        maxi = 0

        for p in prices:
            mini = min(mini, p)
            maxDiff = max(maxDiff, p - mini)

        return maxDiff