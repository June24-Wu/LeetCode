class UF:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.cnt = n
    def find(self,n):
        if n != self.parents[n]:
            self.parents[n] = self.find(self.parents[n])
        return self.parents[n]
    def union(self,a,b):
        a = self.find(a)
        b = self.find(b)
        self.parents[b] = a
        self.cnt -= 1
    def isConnected(self,a,b):
        return self.find(a) == self.find(b)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        length = len(stones)
        uf = UF(length)
        for i in range(length):
            for j in range(i+1,length):
                if (stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]) and uf.isConnected(i,j) == False:
                    uf.union(i,j)
        return length - uf.cnt
            
        