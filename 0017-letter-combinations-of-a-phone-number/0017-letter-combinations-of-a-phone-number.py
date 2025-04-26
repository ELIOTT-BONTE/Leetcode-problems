class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nb_to_letter = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8": "tuv", "9" : "wxyz"}
        if not digits:
            return []
        res = [""]
        for nb in digits:
            temp = []
            for letter in nb_to_letter[nb]:
                for r in res:
                    temp.append(r+letter)
            res = temp
        return res