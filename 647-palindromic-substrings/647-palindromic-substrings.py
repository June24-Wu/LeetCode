class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        def isValid(left,right):
            if left >= right:
                return True
            return dp[left][right]
        ans = 0
        for i in range(1,len(s) + 1):
            for j in range(len(s)-i + 1):
                left = j ; right = j + i - 1
                dp[left][right] = s[left] == s[right] and isValid(left + 1 , right - 1)
                ans += 1 if dp[left][right] == True else 0
        return ans