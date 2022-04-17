class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def dfs(grid,row,col):
            # boundary
            if row < 0 or row >= m or col < 0 or col >=n:
                return
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(grid,row+1,col)
            dfs(grid,row-1,col)
            dfs(grid,row,col+1)
            dfs(grid,row,col-1)
            return
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(grid,i,j)
        return cnt
        
        

        
        