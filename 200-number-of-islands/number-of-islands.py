class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid); n = len(grid[0])
        def dfs(r,c):
            grid[r][c] = "0"
            for i, j in [(1,0),(-1,0),(0,1),(0,-1)]:
                newr, newc = r + i, c + j
                if 0 <= newr < m and 0 <= newc < n and grid[newr][newc] == "1":
                    dfs(newr,newc) 
            return
        ans = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)
        return ans
        