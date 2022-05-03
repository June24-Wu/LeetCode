class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [-prices[0],0,0]
        
        for i in range(1,len(prices)):
            temp = dp.copy()
            dp = [0,0,0]
            dp[0] = max(temp[0],temp[2]-prices[i])
            dp[1] = temp[0] + prices[i]
            dp[2] = max(temp[2],temp[1])
            print(dp)
        return max(dp)
        
        