class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid) and len(grid[0])

        max_sum = 0
        cur_sum = 0

        def dfs(i, j):
            nonlocal max_sum, cur_sum

            is_stuck = True
            for p, q in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= p < m and 0 <= q < n and 0 < grid[p][q]:
                    is_stuck = False

                    # Save value for backtrack.
                    value = grid[p][q]

                    cur_sum += value

                    # Mark cell as visited.
                    grid[p][q] = 0

                    dfs(p, q)

                    # Backtrack
                    cur_sum -= value
                    grid[p][q] = value

            # Cannot move anywhere, DFS is done. So save the sum.
            if is_stuck:
                max_sum = max(max_sum, cur_sum)

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    # Save value for backtrack.
                    cur_sum = value = grid[i][j]

                    # Mark cell as visited.
                    grid[i][j] = 0

                    dfs(i, j)

                    # Backtrack.
                    grid[i][j] = value

        return max_sum