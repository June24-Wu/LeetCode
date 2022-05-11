class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = float("inf")
                else:
                    grid[i][j] = 0
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i >= 1:
                    grid[i][j] = min(grid[i-1][j]+1,grid[i][j])
                if j >= 1:
                    grid[i][j] = min(grid[i][j-1]+1,grid[i][j])
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j] == 0:
                    continue
                if i < n-1:
                    grid[i][j] = min(grid[i+1][j]+1,grid[i][j])
                if j < n-1:
                    grid[i][j] = min(grid[i][j+1]+1,grid[i][j])
                ans = max(ans,grid[i][j])             
        if ans == float("inf") or ans == 0:return -1
        return ans