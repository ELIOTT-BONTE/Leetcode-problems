class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start, combination, sum):
            if sum == target:
                res.append(combination[:])
                return
            elif sum > target:
                return
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                dfs(i, combination, sum+candidates[i])
                combination.pop()
        
        dfs(0, [], 0)
        return res