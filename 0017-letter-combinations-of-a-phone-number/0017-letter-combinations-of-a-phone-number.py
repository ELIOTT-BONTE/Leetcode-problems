class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        key = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        if digits :
            res = [""]
        for d in digits:
            temp = [] # collect new combinations
            for r in res:
                for k in key[d]:
                    temp.append(r+k)
            res = temp

        return res
