class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, sum, path):
            if sum > target:
                return res
            elif sum == target:
                res.append(path[:])
            for i in range(start, len(candidates)):
                sum = sum + candidates[i]
                path.append(candidates[i])
                backtrack(i, sum, path)
                sum = sum - candidates[i]
                path.pop()
        backtrack(0, 0, [])
        return res

            
