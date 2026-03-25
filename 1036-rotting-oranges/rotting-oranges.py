class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid); n = len(grid[0])

        rot = []; total = 0; vis = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rot.append((i,j))
                    vis.add((i,j))
                if grid[i][j] != 0:
                    total += 1
        if total == 0:
            return 0
        ans = 0
        while rot:
            length = len(rot)
            # print(rot,ans)
            for _ in range(length):
                r, c = rot.pop(0)
                for i, j in [(1,0),(0,1),(-1,0),(0,-1)]:
                    newr, newc = r+i, c+j
                    if 0<= newr<m and 0<= newc < n and (newr,newc) not in vis and grid[newr][newc] == 1:
                        vis.add((newr,newc))
                        rot.append([newr,newc])
            ans += 1
        return ans - 1 if len(vis) == total else -1
        