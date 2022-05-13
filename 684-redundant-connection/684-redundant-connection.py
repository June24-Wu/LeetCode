class UF:
    def __init__(self,n):
        self.li = [i for i in range(n+1)]
    def find(self,x):
        if self.li[x] != x:
            self.li[x] = self.find(self.li[x])
        return self.li[x]
    def union(self,a,b):
        a = self.find(a)
        b = self.find(b)
        self.li[b] = a
        return

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max([max(i) for i in edges])
        print(n)
        
        uf = UF(n)
        
        last = None
        for i,j in edges:
            if uf.find(i) == uf.find(j):
                last = [i,j]
            uf.union(i,j)
        # print(last)
        return last
        