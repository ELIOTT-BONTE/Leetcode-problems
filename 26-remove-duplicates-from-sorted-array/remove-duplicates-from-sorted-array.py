class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l , r = 0, 0
        v = -101
        count = 0
        while r < len(nums):
            if nums[r] == v:
                nums[r] = 101
                r += 1
            else:
                count += 1
                v = nums[r]
                nums[r] = 101
                nums[l] = v
                l += 1
                r += 1
                
        return count
