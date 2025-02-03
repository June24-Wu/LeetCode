class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0 for _ in range(5)]
        dp[1] = - prices[0]
        dp[3] = - prices[0]
        for i in range(1,n):
            dp[1] = max(dp[1],dp[0] - prices[i])
            dp[2] = max(dp[2],dp[1] + prices[i])
            dp[3] = max(dp[3],dp[2] - prices[i])
            dp[4] = max(dp[4],dp[3] + prices[i])
            # print(dp)
        return dp[-1]
            
        