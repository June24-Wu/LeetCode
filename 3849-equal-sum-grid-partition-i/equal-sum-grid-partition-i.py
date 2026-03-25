class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0
        m = len(grid); n = len(grid[0])
        for i in range(m):
            for j in range(n):
                total += grid[i][j]
        if total % 2 != 0:
            return False
        curr = 0
        for i in range(m):
            for j in range(n):
                curr += grid[i][j]
                if curr > total // 2:
                    break
                if j == n - 1 and curr == total // 2:
                    return True
            if curr > total // 2:
                break

        curr = 0
        for i in range(n):
            for j in range(m):
                curr += grid[j][i]
                if curr > total // 2:
                    break
                if j == m - 1 and curr == total // 2:
                    return True
            if curr > total // 2:
                break
        
        return False