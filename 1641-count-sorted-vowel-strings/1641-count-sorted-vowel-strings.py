class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        dp = [1,1,1,1,1]
        for i in range(1,n):
            temp = dp.copy()
            dp = [0,0,0,0,0]
            for j in range(len(dp)):
                for k in range(j,len(dp)):
                    dp[k] += temp[j]
        return sum(dp)
        