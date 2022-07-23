class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[ 0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        for i in range(len(word1)+1):
            dp[0][i] = i
        for i in range(len(word2)+1):
            dp[i][0] = i    
        # print(dp)
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
        # print(dp)
        return dp[-1][-1]        