class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = {0:False}
        for i in range(1,n + 1):
            j = 1 ; flag = False
            while j**2 <= i:
                flag = flag or not dp[i - j**2]
                j += 1
                if flag == True:
                    break
            dp[i] = flag
        # print(dp)
        return dp[n]
    
        