class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid) ; n = len(grid[0])
        
        def dfs(row,col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 1:
                return
            grid[row][col] = 1
            for i , j in [(1,0),(0,1),(-1,0),(0,-1)]:
                dfs(row+i,col+j)
            
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for i in range(n):
            dfs(0,i)
            dfs(m-1,i)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1
                    dfs(i,j)
        return ans