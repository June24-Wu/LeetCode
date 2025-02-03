class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0 for _ in range(2*k+1)]
        for i in range(1,len(dp),2):
            dp[i] = -prices[0]
        for i in range(1,len(prices)):
            for j in range(1,len(dp)):
                if j % 2 == 1:
                    dp[j] = max(dp[j],dp[j-1] - prices[i])
                else:
                    dp[j] = max(dp[j],dp[j-1] + prices[i])
        return dp[-1]
        