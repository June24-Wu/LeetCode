class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(5)]
        
        # initialize
        
        dp[1] = - prices[0]
        dp[3] = - prices[0]
        # for loop
        
        for i in range(1,len(prices)):
            dp[1] = max(dp[0] - prices[i],dp[1])
            dp[2] = max(dp[2],dp[1] + prices[i])
            dp[3] = max(dp[3],dp[2] - prices[i])
            dp[4] = max(dp[4],dp[3] + prices[i])
        return dp[-1]