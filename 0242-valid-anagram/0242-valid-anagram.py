from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initalize a hashmap {letter : count}

        count = defaultdict(int)

        for c in s:
            count[c] += 1
        for c in t:
            count[c] -= 1

        return all(val == 0 for val in count.values())