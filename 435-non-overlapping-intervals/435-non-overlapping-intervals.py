class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1],x[0]))
        print(intervals)
        if len(intervals) <= 1:return 0 
        
        right = intervals[0][1]
        cnt = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] < right:
                cnt += 1
            else:
                right = intervals[i][1]
        return cnt
        