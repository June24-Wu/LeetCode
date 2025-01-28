class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid); n = len(grid[0])
        def dfs(r,c):
            curr = grid[r][c]
            grid[r][c] = 0
            for i , j in [(1,0),(-1,0),(0,1),(0,-1)]:
                newr , newc = r + i , c + j
                if 0 <= newr < m and 0 <= newc < n and grid[newr][newc] > 0:
                    curr += dfs(newr,newc)
            return curr
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    ans = max(ans,dfs(i,j))
        return ans
        