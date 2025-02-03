class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minnow = float("inf"); ans = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans

        