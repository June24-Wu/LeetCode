class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0 for _ in range(5)] for _ in range(n)]
        for i in range(5):
            dp[0][i] = 1
        for i in range(1,n):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = dp[i-1][0] + dp[i-1][2]
            dp[i][2] = sum(dp[i-1]) - dp[i-1][2]
            dp[i][3] = dp[i-1][2] + dp[i-1][4]
            dp[i][4] = dp[i-1][0]
        return sum(dp[-1]) % (10**9 + 7)
        