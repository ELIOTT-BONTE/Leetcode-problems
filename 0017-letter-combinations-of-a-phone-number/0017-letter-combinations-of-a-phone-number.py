class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        equivalence = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        def backtrack(start, path):
            if start == len(digits):
                res.append(path)
                return
            for letter in equivalence[digits[start]]:
                path += letter
                backtrack(start+1, path)
                path = path[:-1]
                
        
        backtrack(0, "")
        return res

