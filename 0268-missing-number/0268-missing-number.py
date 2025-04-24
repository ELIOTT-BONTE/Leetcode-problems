class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # gauss formula
        n = len(nums)
        expected_sum = n*(n+1)//2 # direct application of gauss
        actual_sum = 0
        for n in nums:
            actual_sum += n
        return  expected_sum -actual_sum