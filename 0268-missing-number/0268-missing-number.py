class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #compute expected sum
        # 1 + 2 = 3
        # 1 + 2 + 3 = 6
        # 4 => 10
        # 5 => 15
        # general formula : n + (n+1) //2
        n = len(nums)
        expected = (n * (n+1))//2
        #compute difference between expected sum and actuel sum
        actual_sum = 0
        for n in nums:
            actual_sum += n
        return expected - actual_sum