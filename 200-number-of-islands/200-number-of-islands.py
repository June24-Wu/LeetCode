class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid) ; 
        n = len(grid[0])
        def dfs(r,c):
            grid[r][c] = 0
            for i , j in [(1,0),(-1,0),(0,1),(0,-1)]:
                row = r + i ; col = c + j
                if 0 <= row < m and 0 <= col < n and grid[row][col] == "1":
                    dfs(row,col)
            return
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i,j)
        return cnt
        