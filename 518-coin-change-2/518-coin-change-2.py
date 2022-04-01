class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)] 
        dp[0] = 1
        for item in coins:
            for j in range(item,amount+1):
                dp[j] += dp[j-item]
        return dp[-1]
        