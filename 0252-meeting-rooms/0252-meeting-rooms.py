class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        encountered = set()
        for i in intervals:
            for y in range(i[0],i[1]):
                if y in encountered:
                    return False
                encountered.add(y)
        return True