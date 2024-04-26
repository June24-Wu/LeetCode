class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(1,n):
            for j in range(n):
                grid[i][j] += min(grid[i-1][:j] + grid[i-1][j+1:])
        # print(grid)
        return min(grid[-1])
        