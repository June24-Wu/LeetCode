class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxVal = prices[-1]
        profit = 0
        for i in range(len(prices)-2,-1,-1):
            if prices[i] < maxVal:
                profit = max(profit,maxVal-prices[i])
            else:
                maxVal = prices[i]
        return profit
        