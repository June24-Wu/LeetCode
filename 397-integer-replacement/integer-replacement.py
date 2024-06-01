class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(None)
        def dfs(num):
            if num == 1:
                return 0
            if num % 2 == 0:
                return dfs(num//2) + 1
            if num % 2 == 1:
                return min(dfs(num+1),dfs(num-1)) + 1
        return dfs(n)
            
        