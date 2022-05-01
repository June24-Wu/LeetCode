class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [0 for _ in range(length)]
        for i in range(length-1,-1,-1):
            temp = dp.copy()
            dp = [0 for _ in range(length)]
            dp[i] = 1
            for j in range(i+1,length):
                if s[i] == s[j]:
                    dp[j] = temp[j-1] + 2
                else:
                    dp[j] = max(temp[j],dp[j-1])
            # print(dp)
        return dp[-1]
                
        