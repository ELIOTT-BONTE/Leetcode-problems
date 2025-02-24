class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0

        for num in nums:
            if i < 2 or num != nums[i-2]:
                # then insert it
                nums[i] = num
                # and increment pointer
                i += 1
        
        return i
