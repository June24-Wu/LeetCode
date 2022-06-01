class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid) ; n = len(grid[0])
        
        def dfs(row,col,char):
            nonlocal path
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return
            path += char
            grid[row][col] = 0
            dfs(row-1,col,"up,")
            dfs(row+1,col,"down,")
            dfs(row,col+1,"right,")
            dfs(row,col-1,"left,")
            path += "end."
            
        ans = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = ""
                    dfs(i,j,"start,")
                    ans.add(path)
        return len(ans)
                    