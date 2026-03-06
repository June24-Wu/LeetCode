class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : (x[0],-x[1]))
        left = intervals[0][0]
        right = intervals[0][1]
        ans = []
        for i in range(1,len(intervals)):
            l, r = intervals[i]
            if l <= right:
                right = max(right,r)
            else:
                ans.append([left,right])
                left = l
                right = r
        ans.append([left,right])
        return ans
        