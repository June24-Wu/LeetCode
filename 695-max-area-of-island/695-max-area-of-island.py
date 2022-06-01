class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0 ; m = len(grid) ; n = len(grid[0])
        def dfs(row,col):
            nonlocal grid
            nonlocal ans
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            area = dfs(row+1,col) + dfs(row,col+1) + dfs(row-1,col) + dfs(row,col-1) + 1
            ans = max(ans,area)
            return area
        for i in range(m):
            for j in range(n):
                dfs(i,j)
        return ans
        