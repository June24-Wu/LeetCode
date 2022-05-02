class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) ; n = len(grid[0])
        def get(row,col):
            if row < 0 or row >= m or col < 0 or col >=n:
                return float("inf")
            return grid[row][col]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 :continue
                grid[i][j] += min(get(i-1,j),get(i,j-1))
        return grid[-1][-1]
        