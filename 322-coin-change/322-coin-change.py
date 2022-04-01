class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0
        for item in coins:
            for j in range(item,amount+1):
                dp[j] = min(dp[j],dp[j-item] + 1)
        
        if dp[-1] == float("inf"):return -1
        return dp[-1]
        