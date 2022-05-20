class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount+ 1) ]
        dp[0] = 0
        for coin in coins:
            for j in range(coin,len(dp)):
                dp[j] = min(dp[j-coin] + 1 , dp[j])
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]