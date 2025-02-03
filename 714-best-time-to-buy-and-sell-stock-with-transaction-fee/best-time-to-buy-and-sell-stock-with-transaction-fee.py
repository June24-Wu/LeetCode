class Solution:
    def maxProfit(self, prices: List[int], f: int) -> int:
        a = - prices[0] ; b= 0
        for i in prices[1:]:
            t = a
            a = max(a,b - i)
            b = max(b,t + i - f)
        return max(a,b)