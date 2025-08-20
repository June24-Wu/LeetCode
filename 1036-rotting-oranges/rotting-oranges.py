class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total = 0
        rotten = collections.deque()
        m = len(grid); n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    total += 1
                if grid[i][j] == 2:
                    rotten.append((i,j))
                    total -= 1
        if total == 0:
            return 0
        days = -1
        while rotten:
            length = len(rotten)
            for _ in range(length):
                r, c = rotten.popleft()
                for i, j in [(0,1),(0,-1),(1,0),(-1,0)]:
                    newr = r+i; newc=c+j
                    # if 0 <= newr < m and 0 <= newc < n:
                        # print(newr,newc,grid[newr][newc])
                    if 0 <= newr < m and 0 <= newc < n and grid[newr][newc]==1:
                        grid[newr][newc] = 2
                        total -= 1
                        rotten.append((newr,newc))
            days += 1
        return days if total == 0 else -1

