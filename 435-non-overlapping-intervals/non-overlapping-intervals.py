class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0],x[1]))

        left = intervals[0][0]; right = intervals[0][1]
        ans = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] < right:
                ans += 1
                right = min(right,intervals[i][1])
            else:
                left = intervals[i][0]
                right = intervals[i][1]

        return ans
        