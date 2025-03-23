class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        res = [0] * (n+1)

        def dp(i):
            if i == 0:
                res[i] = 0
            else :
                res[i] = res[i // 2] + (i % 2)
        for i in range(0,n+1):
            dp(i)

        return res
        