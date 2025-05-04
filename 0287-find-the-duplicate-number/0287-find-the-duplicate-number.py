from collections import Counter
from heapq import heapify, heappop

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        heap = [[-freq, num] for num, freq in cnt.items()]
        heapify(heap)

        return heappop(heap)[1]