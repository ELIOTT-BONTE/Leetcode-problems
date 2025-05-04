from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        res=[]
        heap = [[-freq, word] for word, freq in count.items()]
        heapify(heap)
        print(heap)
        for i in range(k):
            res.append(heappop(heap)[1])
        return res