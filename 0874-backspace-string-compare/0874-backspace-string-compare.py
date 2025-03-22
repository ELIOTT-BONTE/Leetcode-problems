class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #store strings into stacks
        stackS=[]
        stackT=[]
        #when encountering special character, pop last elem
        for i in s:
            if i == "#":
                if stackS:
                    stackS.pop()
            else:
                stackS.append(i)
        for i in t:
            if i == "#":
                if stackT:
                    stackT.pop()
            else:
                stackT.append(i)
        #compare stacks
        return stackS == stackT