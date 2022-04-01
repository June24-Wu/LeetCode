class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        
        
        for j in range(1,len(dp)):
            for item in wordDict:
                if j >= len(item):
                    dp[j] = (dp[j] or (dp[j-len(item)] and s[j-len(item):j] == item))
        print(dp)
        return dp[-1]
            
                        
            
        