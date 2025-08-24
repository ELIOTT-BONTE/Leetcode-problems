class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # parse s,
        # if s[i] is not in hashmap as a key,
        # check that t[i] is not in hashmap as a value
        # if s[i] is in hashmap as a key,
        # check that t[i] is the value linked to that key
        
        d = defaultdict(str)
        for i in range(len(s)):
            if s[i] in d.keys():
                if t[i] != d[s[i]]:
                    return False
            else:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
        return True