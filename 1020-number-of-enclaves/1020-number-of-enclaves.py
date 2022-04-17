class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid) ; n = len(grid[0])
        def dfs(grid,row,col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return
            if grid[row][col] == 0:
                return
            grid[row][col] = 0
            dfs(grid,row-1,col)
            dfs(grid,row+1,col)
            dfs(grid,row,col-1)
            dfs(grid,row,col+1)
            return
        for i in range(m):
            dfs(grid,i,0)
            dfs(grid,i,n-1)
        for i in range(n):
            dfs(grid,0,i)
            dfs(grid,m-1,i)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
        return cnt