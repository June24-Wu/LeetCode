class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid) ; n = len(grid[0])
        good = set() ; queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    good.add((i,j))
                if grid[i][j] == 2:
                    queue.append((i,j))
        if not good and not queue:
            return 0
        cnt = 0
        while queue:
            if not good:
                return cnt
            length = len(queue)
            for _ in range(length):
                row , col = queue.pop(0)
                for i ,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                    newRow = row + i ; newCol = col + j
                    if 0 <= newRow < m and 0 <= newCol < n and (newRow,newCol) in good:
                        good.remove((newRow,newCol))
                        queue.append((newRow,newCol))
            cnt += 1
        return -1
        