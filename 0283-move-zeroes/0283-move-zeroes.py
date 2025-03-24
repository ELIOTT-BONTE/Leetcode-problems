class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # l and r pointers
        # wwhen r is on a zero, r goes ahead
        # increment zeroes counter by 1
        # when r is on a non zero val, write it to l, move both pointers to the right
        # when l reaches len(nums) - zeroes, write only zeroes until the end

        l, r = 0, 0
        zeroes = 0

        while l <= len(nums) - 1:
            if l > (len(nums) - 1) - zeroes:
                nums[l] = 0
                l += 1

            elif nums[r] == 0:
                r += 1
                zeroes += 1
            else:
                nums[l] = nums[r]
                l += 1
                r += 1
            
        return nums