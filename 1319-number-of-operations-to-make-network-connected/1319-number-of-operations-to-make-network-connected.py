class UF:
    def __init__(self,n):
        self.li = [i for i in range(n)]
        self.setCount = n
    def find(self,x):
        if self.li[x] != x:
            self.li[x] = self.find(self.li[x])
        return self.li[x]
    def union(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.setCount -= 1
        self.li[b] = a
        return
        

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key = lambda x:(x[0],x[1]))
        if len(connections) < n-1:return -1
        uf = UF(n)
        for i , j in connections:
            uf.union(i,j)

        return uf.setCount - 1
        
        