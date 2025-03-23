class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        for c in bin(n)[2:]:
            if c == "1":
                count +=1
        return count