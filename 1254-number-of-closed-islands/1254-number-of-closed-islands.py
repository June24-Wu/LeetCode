class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,row,col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return
            if grid[row][col] == 1:
                return
            grid[row][col] = 1
            dfs(grid,row-1,col)
            dfs(grid,row+1,col)
            dfs(grid,row,col+1)
            dfs(grid,row,col-1) 
            return
        m = len(grid) ; n = len(grid[0])
        for i in range(n):
            dfs(grid,m-1,i)
            dfs(grid,0,i)
        for i in range(m):
            dfs(grid,i,0) ; dfs(grid,i,n-1)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cnt += 1
                    dfs(grid,i,j)
        return cnt