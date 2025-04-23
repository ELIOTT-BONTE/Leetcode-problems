from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        encounteredAnagrams = defaultdict(list)
        for word in strs:
            char_count = tuple(sorted(word))
            encounteredAnagrams[char_count].append(word)
        return list(encounteredAnagrams.values())