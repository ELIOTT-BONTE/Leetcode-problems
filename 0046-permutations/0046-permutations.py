class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = [] # the current permutation being built
        added = set() # the numbers already in the permutation

        def backtrack(added, curr):
            for i in range(len(nums)):
                if len(curr) == len(nums): # permutation finished
                    res.append(curr[:]) # add copy of current candidate
                    return
                if nums[i] not in added:
                    curr.append(nums[i])
                    added.add(nums[i])

                    backtrack(added, curr) # recursive call
                    curr.pop() # backtrack, undo last choice
                    added.remove(nums[i])
        
        backtrack(added, curr)
        return res
