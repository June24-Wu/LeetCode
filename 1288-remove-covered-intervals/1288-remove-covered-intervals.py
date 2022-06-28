class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x :(x[0], - x[1]))
        print(intervals)
        left = intervals[0][0] ; right = intervals[0][1]
        cnt = 0
        for i in range(1,len(intervals)):
            s ,e = intervals[i][0] , intervals[i][1]
            if right >= e:
                cnt += 1
            if e > right:
                left = s ; right = e
        return len(intervals) - cnt