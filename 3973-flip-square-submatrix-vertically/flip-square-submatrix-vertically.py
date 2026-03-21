class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        for i in range(k//2):
            for j in range(k):
                grid[x+i][j+y], grid[x+k-i-1][j+y] = grid[x+k-i-1][j+y], grid[x+i][j+y]
        return grid

        