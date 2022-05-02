class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float("inf") for _ in range(n)]
        dp[src] = 0
        res = float("inf")
        for i in range(k+1):
            temp = dp.copy()
            dp = [float("inf") for _ in range(n)]
            for start , end , cost in flights:
                dp[end] = min(dp[end],temp[start]+cost)
            res = min(res,dp[dst])
            print(dp)
        if res == float("inf"):
            return -1
        return res
        