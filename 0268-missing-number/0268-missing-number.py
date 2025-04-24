from collections import defaultdict

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        encountered = defaultdict(int)
        for i, num in enumerate(nums):
            encountered[i] -= 1 #-1 means should be encountered
            encountered[num] += 1 #+1 means has been encountered
        
        
        for n in encountered.keys():
            if encountered[n] == -1:
                return n
        return len(nums)