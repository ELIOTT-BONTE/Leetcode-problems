class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        added = set()

        # if number is already in permutation, skip it

        def backtracking(candidate):
            
            if len(candidate) == len(nums): # valid permutation
                res.append(candidate[:]) # use a copy of candidate
            for n in nums:
                if n in added:
                    continue #skip this number
                added.add(n)
                candidate.append(n)
                backtracking(candidate)
                candidate.pop() # backtrack, so pop last thing we added
                added.remove(n)
            
        backtracking([])
        return res
            