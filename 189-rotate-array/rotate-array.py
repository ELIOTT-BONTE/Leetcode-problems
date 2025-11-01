class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mem = 0
        for i in range(k):
            mem = nums.pop()
            nums.insert(0,mem)