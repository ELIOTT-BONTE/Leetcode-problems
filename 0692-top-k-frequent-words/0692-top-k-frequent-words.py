from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        cnt = Counter(words)
        heap = [(-freq, word) for word, freq in cnt.items()]
        heapify(heap)

        for i in range(k):
            res.append(heappop(heap)[1])
        
        return res