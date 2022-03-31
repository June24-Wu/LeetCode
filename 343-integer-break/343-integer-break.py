class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3,len(dp)):
            for j in range(0,i-1):
                dp[i] = max(dp[i],max((i-j)*j,dp[i-j]*j))
        print(dp)
        return dp[-1]
        