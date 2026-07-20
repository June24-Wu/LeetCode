class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x : (x[0],x[1]))

        left = intervals[0][0]; right = intervals[0][1]
        ans = 0
        # print(intervals)
        for i in range(1,len(intervals)):
            # print(intervals[i][1])
            if intervals[i][0] < right:
                ans += 1
                right = min(intervals[i][1],right)
            else:
                left = intervals[i][0]
                right = intervals[i][1]
        return ans

        