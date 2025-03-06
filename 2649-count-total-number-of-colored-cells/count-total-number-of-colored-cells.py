class Solution:
    def coloredCells(self, n: int) -> int:
        def dfs(n):
            if n == 1:
                return 1
            else:
                return 4 * (n - 1) + dfs(n-1)
        return dfs(n)
        