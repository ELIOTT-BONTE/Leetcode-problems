from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        encountered = set()
        res = 0

        while r < len(s):
            
            
            
            if s[r] not in encountered:
                diff = r - l+1
                res = max(res, diff)
                encountered.add(s[r])
                r += 1
                
                
            else :
                encountered.remove(s[l])
                l += 1
        return res
