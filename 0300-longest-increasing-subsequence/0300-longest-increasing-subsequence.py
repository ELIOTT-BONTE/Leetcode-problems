class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1
        for index, num in enumerate(nums):
            for antecedant in range(0, index):
                if nums[antecedant] < num:

                    dp[index] = max(dp[index], dp[antecedant] + 1)
                    res = max(res, dp[index])
        return res