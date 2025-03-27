from math import sqrt

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        return sorted(points, key=lambda p: sqrt((0-p[0])**2 + (0-p[1])**2))[:k]