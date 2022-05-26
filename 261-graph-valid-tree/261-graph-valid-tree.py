class UF:
    def __init__(self,n:int):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.count = n
    def find(self,n):
        if self.parents[n] != n:
            self.parents[n] = self.find(self.parents[n])
        return self.parents[n]
    def union(self,a,b):
        a = self.find(a) ; b = self.find(b)
        if self.size[a] < self.size[b]:
            temp = a ; a = b ; b = temp
        self.size[a] += self.size[b]
        self.parents[b] = a
        self.count -= 1
        return
    def isConnected(self,a,b):
        return self.find(a) == self.find(b)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UF(n)
        for a , b in edges:
            if uf.isConnected(a,b):
                return False
            uf.union(a,b)
        return uf.count == 1
        