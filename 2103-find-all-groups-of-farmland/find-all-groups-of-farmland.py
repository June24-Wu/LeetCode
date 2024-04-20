class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land) ; n = len(land[0])
        def dfs(row,col):
            if land[row][col] == 0:
                return [-1,-1]
            land[row][col] = 0
            rt = [row,col]
            # print(row,col)
            for i , j in [(1,0),(-1,0),(0,1),(0,-1)]:
                newr , newc = row + i , col + j
                if 0 <= newr < m and 0 <= newc < n and land[newr][newc] == 1:
                    maxr , maxc = dfs(newr,newc)
                    rt[0] = max(rt[0],maxr)
                    rt[1] = max(rt[1],maxc)
            # print(row,col,rt)
            return rt
        ans = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    r2 , c2 = dfs(i,j)
                    ans.append([i,j,r2,c2])
        return ans

        