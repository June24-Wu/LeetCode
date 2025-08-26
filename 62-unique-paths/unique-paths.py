class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[0][0] = 1
        def get(r,c):
            if 0 <= r < m and 0 <= c < n:
                return grid[r][c] 
            return 0
        for i in range(m):
            for j in range(n):
                grid[i][j] += get(i-1,j) + get(i,j-1)
        # print(grid)
        return grid[-1][-1]
        