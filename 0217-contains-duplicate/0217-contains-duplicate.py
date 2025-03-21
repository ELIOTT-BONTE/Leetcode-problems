class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        encountered = set()
        for i in nums:
            if i in encountered:
                return True
            encountered.add(i)
        return False