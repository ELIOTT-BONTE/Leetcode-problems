class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        key = {
            "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",
            "7":"pqrs","8":"tuv","9":"wxyz"
        }

        res = [""]
        # for d in digits:
        #     temp = []
        #     for char in key[d]:
        #         for r in res:
        #             temp.append(r + char)
        #     res = temp

        for d in digits:
            res = [r + k for r in res for k in key[d]]
        
        return res