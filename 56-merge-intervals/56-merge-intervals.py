class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0],x[1]))
        merge = []
        if len(intervals) <= 1: return intervals
        
        left = intervals[0][0]
        right = intervals[0][1]
        
        for i in range(1,len(intervals)):
            if intervals[i][0] <= right:
                right = max(right,intervals[i][1])
            else:
                merge.append([left,right])
                left = intervals[i][0]
                right = intervals[i][1]
        merge.append([left,right])
        return merge
            
        
        