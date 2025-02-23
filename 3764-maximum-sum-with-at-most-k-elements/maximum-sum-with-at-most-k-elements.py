class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        a = []
        for i in range(n):
            row = grid[i]
            row.sort(reverse = True)
            a = a + row[:limits[i]]
        a.sort(reverse = True)
        # print(a)
        return sum([i for i in a[:k]])
        