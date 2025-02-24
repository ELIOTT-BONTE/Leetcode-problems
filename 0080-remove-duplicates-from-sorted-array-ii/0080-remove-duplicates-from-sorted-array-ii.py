from collections import defaultdict

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0 #points to the last space where we can insert values

        for num in nums:
            if i < 2 or num != nums[i-2]: # chec if we can insert the current iterated number
                nums[i] = num
                i += 1
        return i