class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = 0,0
        while r <= len(haystack):
            if haystack[l:r+1] == needle: # r+1 because last elem excluded
                return l
            elif haystack[l:r+1] == needle[:r-l+1]:
                r += 1
            else:
                l += 1 
                r = l+1
        return -1