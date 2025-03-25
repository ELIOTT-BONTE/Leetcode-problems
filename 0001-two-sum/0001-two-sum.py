from collections import defaultdict

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #hashmap {key:value}
        #iterate through array
        #check difference target - val
        #if difference in hashmap, then
        #return both
        #otherwise, add iterated val and index

        encountered = defaultdict(int)
        i = 0
        while i <= len(nums)-1:
            diff = target - nums[i]
            if diff in encountered:
                return encountered[diff],i
            else:
                encountered[nums[i]] = i
            i += 1
            