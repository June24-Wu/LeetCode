class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix) ; n = len(matrix[0])
        def get(row,col):
            if 0 <= row < m and 0 <= col < n:
                return int(dp[row][col])
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(get(i-1,j),get(i,j-1),get(i-1,j-1)) + 1
                    ans = max(dp[i][j],ans)
        return ans**2
        