class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        minVal = prices[0]
        returnVal = 0
        for i in range(1,len(prices)):
            if prices[i] < minVal:
                minVal = prices[i]
            else:
                if prices[i] - minVal <= fee:
                    continue
                else:
                    returnVal += prices[i] - minVal - fee
                    minVal = prices[i] - fee
        return returnVal
        