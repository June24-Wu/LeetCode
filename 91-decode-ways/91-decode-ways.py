class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        dp[1] = 2 if int(s[:2]) <= 26 and s[1] != "0" else 1
        if s[1] =="0" and s[0] >= "3":
            return 0
        for i in range(2,len(s)):
            if s[i] == "0":
                if int(s[i - 1]) >= 3 or int(s[i - 1]) == 0:
                    return 0
                dp[i] = dp[i - 2]
                continue
            if s[i - 1] == "0":
                dp[i] = dp[i - 1]
                continue
            if int(s[i-1:i+1]) <= 26:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i - 1]
        print(dp)
        return dp[-1]
        
        