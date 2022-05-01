class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0 for _ in range(len(text1))]
        
        
        for item in text2:
            for j in range(len(dp)-1,-1,-1):
                if text1[j] == item:
                    if dp[:j] == []:
                        dp[j] = 1
                    else:
                        dp[j] = max(dp[:j]) + 1
            # print(dp)
        return max(dp)