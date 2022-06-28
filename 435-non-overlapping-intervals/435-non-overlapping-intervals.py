class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0] , x[1]))
        cnt = 0 
        left = intervals[0][0] ; right = intervals[0][1]
        for i in range(1,len(intervals)):
            s , e = intervals[i][0] , intervals[i][1]
            if right > s:
                cnt += 1
                right = min(right,e)
            else:
                left - s ; right = e
        print(intervals)
        return cnt
        # print(intervals)
        