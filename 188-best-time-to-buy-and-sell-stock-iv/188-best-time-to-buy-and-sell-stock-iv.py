class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if prices == []: return 0
        dp = [0 for _ in range(2*k+1)]

        # initialize
        
        for i in range(len(dp)):
            if i % 2 == 1:
                dp[i] = -prices[0]
        
        # for loop
        
        for i in range(1,len(prices)):
            for trans in range(1,2*k + 1):
                if trans % 2 == 1:
                    dp[trans] = max(dp[trans],dp[trans-1] - prices[i])
                else:
                    dp[trans] = max(dp[trans],dp[trans-1] + prices[i])
        return dp[-1]
        