class UF:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.count = n
    def find(self,index):
        if index != self.parents[index]:
            self.parents[index] = self.find(self.parents[index])
        return self.parents[index]
    def union(self,a,b):
        a = self.find(a) ; b = self.find(b)
        self.parents[b] = a
        self.count -= 1
        return
    def isConected(self,a,b):
        return self.find(a) == self.find(b)
    def getCount(self):
        return self.count
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UF(n)
        for i , j in edges:
            if not uf.isConected(i,j):
                uf.union(i,j)
        return uf.getCount()
        