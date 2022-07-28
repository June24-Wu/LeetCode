class UF:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.cnt = n
    def find(self,index):
        if index != self.parents[index]:
            self.parents[index] = self.find(self.parents[index])
        return self.parents[index]
    def union(self,a,b):
        a = self.find(a)
        b = self.find(b)
        self.cnt -= 1
        self.parents[b] = self.parents[a]
        return
    def isConnetced(self,a,b):
        return self.find(a) == self.find(b)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        table = []
        for i in range(n):
            for j in range(i+1,n):
                x1 , y1 = points[i]
                x2 , y2  = points[j]
                table.append((abs(x1-x2) + abs(y1-y2),i,j))
        heapq.heapify(table)
        uf = UF(n)
        ans = 0
        while uf.cnt != 1 and table:
            val , p1 , p2 = heapq.heappop(table)
            if uf.isConnetced(p1,p2):
                continue
            else:
                uf.union(p1,p2)
                ans += val
        return ans
        
        