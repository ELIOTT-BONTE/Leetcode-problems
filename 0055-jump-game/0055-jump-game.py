class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = (len(nums)) *[0]

        for i, n in enumerate(nums):
            if n != 0:
                for j in range(0, n):
                    if (i+j) < len(reach)-1:
                        reach[i+j] = 1
                    elif (i+j) == len(reach)-1:
                        return True
            elif n == 0:
                if i == len(reach)-1:
                    return True
                elif reach[i] == 0:
                    return False