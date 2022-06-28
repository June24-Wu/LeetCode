class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        ans = []
        left = intervals[0][0] ; right = intervals[0][1]
        for i in range(1,len(intervals)):
            start , end = intervals[i][0] , intervals[i][1]
            if start <= right:
                right = max(right,end)
            else:
                ans.append([left,right])
                left = start ; right = end
        ans.append([left,right])
        return ans