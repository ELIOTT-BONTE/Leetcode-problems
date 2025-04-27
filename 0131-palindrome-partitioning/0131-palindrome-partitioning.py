class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start, path):
            
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start+1, len(s)+1):
                candidate = s[start:end]
                if candidate == candidate[::-1]:
                    path.append(candidate)
                    backtrack(end, path)
                    path.pop()



            

        

        backtrack(0, [])
        return res