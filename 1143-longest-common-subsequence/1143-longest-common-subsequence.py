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
#         dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
#         max_Val = 0
#         for i in range(1,len(text1)+1):
#             for j in range(1,len(text2)+1):
#                 if text1[i-1] == text2[j-1]:
#                     dp[i][j] = dp[i-1][j-1] + 1
#                     max_Val = max(dp[i][j],max_Val)
#         return max_Val
        