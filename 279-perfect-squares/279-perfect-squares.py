class Solution:
    def numSquares(self, n: int) -> int:
        if n ==1:return 1
        items = [i**2 for i in range(1,n//2 + 1)]
        
        dp=[float("inf") for _ in range(n+1)]
        
        dp[0] = 0
        
        for item in items:
            for j in range(item,n+1):
                dp[j] = min(dp[j],dp[j-item]+1)

        return dp[-1]        