from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        encountered = defaultdict(int)
        for i,v in enumerate(nums):
            diff = target - v
            if diff in encountered :
                return i, encountered[diff]
            encountered[v] = i