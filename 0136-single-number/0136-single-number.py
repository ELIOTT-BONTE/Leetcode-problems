from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #initate a hashmap

        #when a value in hashmap reaches 2, return its key

        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        for n,v in count.items():
            if v == 1:
                return n