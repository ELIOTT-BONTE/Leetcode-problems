class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * (len(nums))
        right = [0] * (len(nums))
        res = [0] * len(nums)

        for n in range(len(nums)):
            left[n] = 1 if n == 0 else left[n-1] * nums[n-1]
        
        n = len(nums)-1
        while n >= 0:
            right[n] = 1 if n == len(nums)-1 else right[n+1] * nums[n+1]
            n -= 1
        for n in range(len(nums)):
            res[n] = left[n]*right[n]

        return res