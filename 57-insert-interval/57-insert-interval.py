class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: (x[0],x[1]))
        
        left = intervals[0][0] ; right = intervals[0][1] 
        rt = []
        
        for i in range(1,len(intervals)):
            if intervals[i][0] <= right:
                right = max(intervals[i][1],right)
            else:
                rt.append([left,right])
                left = intervals[i][0]
                right = intervals[i][1]
        rt.append([left,right])
        return rt