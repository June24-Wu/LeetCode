class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid) ; n = len(grid[0])
        queue = []
        
        def dfs(row,col):
            if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                queue.append((row,col))
                grid[row][col] = 0
                for i , j in [(1,0),(0,1),(-1,0),(0,-1)]:
                    dfs(row+i,col+j)
        for index in range(m*n):
            i = index // n ; j = index % n
            if grid[i][j] == 1:
                dfs(i,j)
                break
        ans = -1
        print(queue)
        while queue:
            length = len(queue)
            for _ in range(length):
                row , col = queue.pop(0)
                if grid[row][col] == 2:
                    continue
                elif grid[row][col] == 1:
                    return ans
                else:
                    grid[row][col] = 2
                    for i , j in [(1,0),(0,1),(-1,0),(0,-1)]:
                        if 0 <= row + i < m and 0 <= col + j < n and grid[row + i][col + j] != 2:
                            queue.append((row+i,col+j))
            ans += 1
        return -1
        