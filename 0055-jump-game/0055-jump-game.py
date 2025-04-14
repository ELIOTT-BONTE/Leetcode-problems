class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        maxReach = 0

        for index, num in enumerate(nums):
            if maxReach < index:
                return False
            maxReach = max(maxReach, index + num)
        return True
