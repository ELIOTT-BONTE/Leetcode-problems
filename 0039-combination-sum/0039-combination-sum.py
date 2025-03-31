class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # all elems are unique, so to avoid duplicate, move start of iteration forward each iteration

        def dfs(start, combination, sum):
            if sum == target: # if sum is target, add combination
                res.append(combination[:])
                return
            elif sum > target:  # if sum more than target, stop
                return
            for i in range(start, len(candidates)): # if sum less than target, add next candidate (can be same one or a latter one)
                combination.append(candidates[i])
                dfs(i, combination, sum+candidates[i])
                combination.pop()
        
        dfs(0, [], 0)
        return res