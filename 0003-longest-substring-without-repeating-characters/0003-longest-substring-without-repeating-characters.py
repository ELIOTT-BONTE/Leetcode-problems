class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #left and right pointers
        #check if right pointed value in hash
        #if yes, move l until it is not anymore
        #if no, add it to hash, then compute r - l

        l, r = 0, 0
        maxi = 0
        encountered = set()
        while r < len(s):
            if s[r] in encountered:
                encountered.remove(s[l])
                l += 1
            else:
                encountered.add(s[r])
                
                r += 1
                maxi = max(maxi, r - l)
        return maxi