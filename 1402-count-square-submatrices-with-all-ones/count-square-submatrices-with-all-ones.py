class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix); n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        def get(r,c):
            if 0 <= r < m and 0 <= c < n:
                return dp[r][c]
            return 0
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    print(i,j,get(i-1,j),get(i,j-1),1)
                    dp[i][j] = min(get(i-1,j),get(i,j-1),get(i-1,j-1)) + 1
                    ans += dp[i][j]
        return ans 

        