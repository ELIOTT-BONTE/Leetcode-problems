from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True
            for end in range(start+1, len(s)+1):
                if end not in seen and s[start:end] in words:
                    seen.add(end)
                    queue.append(end)
        return False