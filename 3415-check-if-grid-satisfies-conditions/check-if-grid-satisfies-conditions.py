class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m = len(grid) ; n = len(grid[0])
        for j in range(n):
            v = grid[0][j]
            for i in range(m):
                if grid[i][j] != v:
                    return False
        for i in range(1,n):
            if grid[0][i] == grid[0][i-1]:
                return False
        return True

        