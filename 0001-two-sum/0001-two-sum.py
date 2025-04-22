from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        encountered = defaultdict(int)
        for index, num in enumerate(nums):
            complement = target - num
            if complement in encountered.keys():
                return [index, encountered[complement]]
            encountered[num] = index
