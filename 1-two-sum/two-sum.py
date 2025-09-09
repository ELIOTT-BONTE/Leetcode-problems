from collections import defaultdict

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # use dict val:index
        # iterate through array
        # calculate difference between current val and target
        # if difference in dict[val]
        # return i, dict[val]
        # else, add val:i to dict

        i = 0
        encountered = defaultdict(int)
        while i < len(nums):
            diff = target - nums[i]
            if diff in encountered.keys():
                return [i, encountered[diff]]
            encountered[nums[i]] = i
            i += 1
        return False