class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        long = s1 if len(s1) >= len(s2) else s2
        short = s1 if len(s1) < len(s2) else s2
        dp = [0 for _ in range(len(long))]
        
        for i in range(len(short)):
            for j in range(len(long)-1,-1,-1):
                if short[i] == long[j]:
                    if j == 0:
                        dp[j] = ord(short[i])
                    else:
                        dp[j] = max(dp[j],max(dp[:j]) + ord(short[i]))
            print(dp)
        res = 0
        for i in s1:
            res += ord(i)
        for j in s2:
            res += ord(j)
        return res - 2* max(dp)