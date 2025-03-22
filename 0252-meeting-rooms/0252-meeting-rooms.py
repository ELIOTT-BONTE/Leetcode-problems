class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort intervals depending on their first element
        intervals.sort(key=lambda interval : interval[0])

        print(intervals)

        # check if second element of i is more than i+1
        # if yes, return False
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False

        # after iterating through all intervals, return True

        return True