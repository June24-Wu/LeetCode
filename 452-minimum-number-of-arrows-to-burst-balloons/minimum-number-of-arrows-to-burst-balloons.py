class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : (x[0],x[1]))
        print(points)
        ans = 0
        left, right = points[0]
        for i in range(1,len(points)):
            l, r = points[i]
            if l <= right:
                right = min(right,r)
            else:
                ans += 1
                left = l
                right = r
        return ans + 1
        