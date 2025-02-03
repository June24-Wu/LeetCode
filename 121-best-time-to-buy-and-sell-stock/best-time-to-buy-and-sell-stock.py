class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        li = [0 for _ in range(n)]
        maxv = - float("inf")
        for i in range(n-1,-1,-1):
            li[i] = maxv
            maxv = max(maxv,prices[i])
        ans = 0
        for i in range(n):
            ans = max(ans,li[i] - prices[i])
        return ans

        