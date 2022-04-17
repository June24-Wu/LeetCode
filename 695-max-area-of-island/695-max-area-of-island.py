class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        cnt = 0
        m = len(grid) ; n = len(grid[0])
        def dfs(grid,row,col):
            nonlocal cnt
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return 1 + dfs(grid,row+1,col) + dfs(grid,row-1,col) + dfs(grid,row,col+1) + dfs(grid,row,col-1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = max(cnt,dfs(grid,i,j))
        return cnt
        