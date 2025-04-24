class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #bit manipulation
        #XOR each number with its index
        #when the two are present in the equation, they cancel each other
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing