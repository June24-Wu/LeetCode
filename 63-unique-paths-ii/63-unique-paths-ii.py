class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid) ; n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        def get(row,col):
            if 0 <= row < m and 0 <= col < n:
                return dp[row][col]
            return 0
        if grid[0][0] == 1:
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or (i== 0 and j == 0):
                    continue
                else:
                    dp[i][j] = get(i-1,j) + get(i,j-1)
        # print(dp)
        return dp[-1][-1]
                
        