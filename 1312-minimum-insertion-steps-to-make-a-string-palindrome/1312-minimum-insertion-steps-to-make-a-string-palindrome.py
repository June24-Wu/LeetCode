class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        dp = [0 for _ in range(length)]
        
        for i in range(length-1,-1,-1):
            temp = dp.copy()
            dp = [0 for _ in range(length)]
            for j in range(i+1,length):
                if s[i] == s[j]:
                    dp[j] = temp[j-1]
                else:
                    dp[j] = min(temp[j],dp[j-1]) + 1
            # print(dp)
        return dp[-1]
        