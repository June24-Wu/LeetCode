class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        
        dp[0] , dp[1] = 1,1
        
        for i in range(2,len(dp)):
            for j in range(1,i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]
        