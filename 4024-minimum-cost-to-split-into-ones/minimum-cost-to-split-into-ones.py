class Solution:
    def minCost(self, n: int) -> int:
        
        @cache
        def dfs(n):
            if n == 1:
                return 0
            if n == 2:
                return 1
            if n == 3:
                return 3
            a = n // 2
            b = n - a
            return a * b + dfs(a) + dfs(b)
        return dfs(n)
        