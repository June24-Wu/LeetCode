class UF:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
    def find(self,index):
        print(index)
        if index != self.parents[index]:
            self.parents[index] = self.find(self.parents[index])
        return self.parents[index]
    def union(self,a,b):
        a = self.find(a) ; b = self.find(b)
        self.parents[b] = a
    def isConnected(self,a,b):
        return self.find(a) == self.find(b)

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        island = [[ 0 for i in range(n)] for _ in range(m)]
        uf = UF(m*n)
        cnt = 0 ; ans = []
        for row , col in positions:
            if island[row][col] != 0:
                ans.append(cnt)
            else:
                island[row][col] = 1 ; cnt += 1
                for x , y in [(0,1),(1,0),(-1,0),(0,-1)]:
                    newRow = row + x ; newCol = col + y
                    if 0 <= newRow < m and 0 <= newCol < n and island[newRow][newCol] == 1:
                        # print(row,m,col)
                        # print(newRow,newCol)
                        a = row * n + col ; b = newRow * n + newCol
                        # print(a,b)
                        if not uf.isConnected(a,b):
                            uf.union(a,b)
                            cnt -= 1
                ans.append(cnt)
        return ans
                        
            