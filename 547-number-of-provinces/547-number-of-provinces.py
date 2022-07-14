class UF:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.cnt = n
    def find(self,index):
        if self.parents[index] != index:
            self.parents[index] = self.find(self.parents[index])
        return self.parents[index]
    def union(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.cnt -= 1
            self.parents[b] = a
        return
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected) ; n = len(isConnected[0])
        a = []
        for i in range(m):
            for j in range(n):
                if i != j and isConnected[i][j] == 1 and [j,i] not in a:
                    a.append([i,j])
        uf = UF(m)
        for i , j in a:
            uf.union(i,j)
        return uf.cnt
            
        