class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x : x[0])
        i = 0
        while i < len(intervals):
            # sort intervals by ascending start
            # take first elem of first interval
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            # while beginning of next interval is less than current end,
            while i +1 < len(intervals) and intervals[i+1][0] <= curr_end:
                curr_end = max(intervals[i+1][1], curr_end)
                i += 1
            res.append([curr_start, curr_end])
            i += 1
            # take end of next interval as current end
        return res