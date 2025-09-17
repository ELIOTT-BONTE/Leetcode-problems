class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        encountered = set()
        res = 0
        while r < len(s):
            # if r is new, incorporate it to encountered letters
            if s[r] not in encountered:
                encountered.add(s[r])
                r += 1
                res = max(res, r - l)
            else:
                encountered.remove(s[l])
                l += 1

        return res
            
            # if r is in encountered letters, remove char pointed to by l, and move l one space to the right