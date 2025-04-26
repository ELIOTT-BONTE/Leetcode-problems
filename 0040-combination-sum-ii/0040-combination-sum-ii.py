class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(start, sum, path):
            if sum > target:
                return
            elif sum == target:
                res.append(path[:])
            for index, i in enumerate(range(start, len(candidates))):
                if index > 0 and candidates[i] == candidates[i-1]:
                    continue
                sum = sum + candidates[i]
                path.append(candidates[i])
                backtrack(i+1, sum, path)
                sum = sum - candidates[i]
                path.pop()
        backtrack(0, 0, [])
        return res