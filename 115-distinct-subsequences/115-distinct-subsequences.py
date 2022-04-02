class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0 for _ in range(len(t)+1)]
        dp[0] = 1
        
        for item in s:
            for j in range(len(dp)-1,0,-1):
                if t[j-1] == item:
                    dp[j] += dp[j-1]
                    # break
            # print(dp)
        return dp[-1]
        