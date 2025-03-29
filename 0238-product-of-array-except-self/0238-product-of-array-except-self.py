class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # built "left" (consisting of the multiplication of all that's left of n)
        # build "right"
        # multiply them
        res = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            res[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        
        return res