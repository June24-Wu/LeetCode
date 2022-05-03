class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens  , lenp = len(s) , len(p)
        dp = [[False for _ in range(lenp+1)] for _ in range(lens + 1)]
        def __isMatch(i,j):
            if i == 0 :
                return False
            if p[j-1] == '.':
                return True
            return s[i-1] == p[j-1]
        dp[0][0] = True
        for i in range(lens+1):
            for j in range(1,lenp+1):
                if p[j-1] == "*":
                    if j == 1:return False
                    dp[i][j] = dp[i][j-2]
                    if __isMatch(i,j-1) and dp[i][j] == False:
                        dp[i][j] = dp[i-1][j]
                else:
                    if __isMatch(i,j):
                        dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]
        
            
        