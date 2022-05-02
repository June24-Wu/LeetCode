class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        
        for i in range(length-1,-1,-1):
            for j in range(i+1,length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i][j-1]) + 1
        # print(dp)
        return dp[0][-1]
        