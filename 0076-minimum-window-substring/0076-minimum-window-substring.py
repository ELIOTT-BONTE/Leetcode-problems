from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l, r = 0, 0
        targetSet = defaultdict(int)
        encounteredSet = defaultdict(int)
        for char in t:
            targetSet[char] += 1


        while r < len(s):
            newLetter= s[r]
            if newLetter in targetSet.keys():
                encounteredSet[newLetter] += 1
                while all(encounteredSet[char] >= targetSet[char] for char in targetSet):
                    # check if new candidate is the shortest one so far
                    if res == "" or len(s[l:r+1]) < len(res):
                        res = s[l:r+1]
                    lostLetter = s[l]
                    if lostLetter in targetSet.keys():
                        encounteredSet[lostLetter] -= 1
                    l += 1
            r += 1
            
        return res