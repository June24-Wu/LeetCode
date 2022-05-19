class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        li = []
        for index , (x,y) in enumerate(points):
            li.append([index,x**2+y**2])
        li.sort(key = lambda x : (x[1]))
        ans = []
        # print(li)
        for i in range(k):
            ans.append(points[li[i][0]])
        return ans
            
        