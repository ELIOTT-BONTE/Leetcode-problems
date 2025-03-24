from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        encountered = set()
        res = []
        for n in nums:
            if n in encountered:
                encountered.remove(n)
            else:
                encountered.add(n)
        return next(iter(encountered))
