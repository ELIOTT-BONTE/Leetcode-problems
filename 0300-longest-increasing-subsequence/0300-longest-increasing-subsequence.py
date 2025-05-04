class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) # to store each potential end of subsequence
        res = 1

        for index, candidate in enumerate(dp):
            if index > 0:
                for j in range(index):
                    if nums[j] < nums[index]:
                        dp[index] = max(dp[index], dp[j] + 1)
                    res = max(dp[index], res)
        return res

