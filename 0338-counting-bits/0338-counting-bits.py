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
                res[i] = res[i // 2] + (i % 2) # number of bits is derived from number of bit of half
                # indeed, left shift of 4 = 8
                # left shift of 4 + 1bit = 9...
        for i in range(0,n+1):
            dp(i)

        return res
        