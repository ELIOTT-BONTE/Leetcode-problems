class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bitwise manipulation
        #perform XOR on the bit rep of all elemes
        # each double elem will cancel each other, leaving only the unique one
        res = 0
        for n in nums:
            res ^= n
        return res
