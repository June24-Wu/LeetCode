class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if intervals == []:
            return True
        intervals.sort(key = lambda x : (x[0],x[1]))
        endMax = intervals[0][1]
        for i in range(1,len(intervals)):
            start = intervals[i][0] ; end = intervals[i][1]
            if start < endMax:
                return False
            else:
                endMax = end
        return True
        