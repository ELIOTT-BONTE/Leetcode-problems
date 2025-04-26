class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # use backtracking

        # try something
        # return if it's good
        # keep exploring if on the right track
        # pop if it's bad
        res = []

        def backtrack(start, path):
            # save a copy of current path
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        

        backtrack(0, [])
        return res

                