class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return  # prune

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue  # skip duplicates

                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])  # move to i+1 (no reuse)
                path.pop()

        backtrack(0, [], 0)
        return res
