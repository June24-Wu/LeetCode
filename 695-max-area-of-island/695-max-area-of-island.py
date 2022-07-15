class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid) ; n = len(grid[0])
        def dfs(r,c):
            if grid[r][c] == 0:
                return 0
            area = 1
            grid[r][c] = 0
            for i , j in [(1,0),(-1,0),(0,1),(0,-1)]:
                row = r + i  ; col = c + j
                if 0 <= row < m and 0 <= col < n and grid[row][col] != 0:
                    area += dfs(row,col)
            return area
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans,dfs(i,j))
        return ans
                