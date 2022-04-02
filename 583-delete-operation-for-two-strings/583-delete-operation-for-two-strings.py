class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        long = word1 if len(word1) >= len(word2) else word2
        short = word1 if len(word1) < len(word2) else word2
        
        dp = [0 for _ in range(len(long))]
        
        
        for item in short:
            for j in range(len(dp)-1,-1,-1):
                if long[j] == item:
                    if j == 0:
                        dp[j] = 1
                    else:
                        dp[j] = max(dp[:j]) + 1
            print(dp)
        length = max(dp)
        return len(word1) + len(word2) - 2 * length