class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for num in range(1,n):
            for j in range(num,n+1):
                dp[j] = max(dp[j],dp[j-num]*num)
        return dp[-1]
        