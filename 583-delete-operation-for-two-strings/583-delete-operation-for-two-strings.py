class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) ; n  = len(word2)
        
        @cache
        def dfs(idx1,idx2):
            if idx1 == m:
                return n - idx2
            if idx2 == n:
                return m - idx1
            if word1[idx1] != word2[idx2]:
                return min(dfs(idx1+1,idx2)+1,dfs(idx1,idx2+1)+1,dfs(idx1+1,idx2+1) + 2)
            return dfs(idx1+1,idx2+1)
        return dfs(0,0)
        