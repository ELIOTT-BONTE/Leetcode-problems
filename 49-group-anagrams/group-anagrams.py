from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # compute dict for word
        # maps letters to their count

        res = defaultdict(list)
        
        for word in strs:
            v = [0]*26
            for letter in word:
                v[ord(letter)-97] += 1
            res[tuple(v)].append(word)
        return res.values()