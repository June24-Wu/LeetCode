class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid); n = len(grid[0])

        def cal(row,col):
            if 1 <= row < m and 1 <= col < n:
                return grid[row][col] + grid[row-1][col] + grid[row][col-1] - grid[row-1][col-1]
            elif row == 0:
                return grid[row][col] + grid[row][col-1]
            elif col == 0:
                return grid[row][col]  + grid[row-1][col]
        if grid[0][0] > k:
            return 0
        ans = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                grid[i][j] = cal(i,j)
                if grid[i][j] <= k:
                    ans += 1
                else:
                    break
        return ans



        