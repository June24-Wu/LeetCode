class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [ float("inf") for i in range(amount+1)]
        dp[0] = 0
        for i in coins:
            for j in range(i,amount+1):
                dp[j] = min(dp[j-i]+1,dp[j])
        if dp[-1] == float("inf"):return -1
        # return 3
        return dp[-1]
                
        