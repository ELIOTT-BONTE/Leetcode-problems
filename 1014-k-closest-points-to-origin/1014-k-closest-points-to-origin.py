# bruteforce

import math
import numpy as np

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # order points with lambda function x: x[0]**2+x[1]**2
        # return k first elements
        points.sort(key = lambda x: x[0]**2+x[1]**2)
        return points[:k]
