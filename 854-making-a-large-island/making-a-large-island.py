class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        original = copy.deepcopy(grid)
        n = len(grid) ; dm = collections.defaultdict(tuple)
        def dfs(r,c):
            nonlocal grid
            if grid[r][c] != 1:
                return 0
            grid[r][c] = -1
            rt = 1
            for i , j in [(1,0),(-1,0),(0,1),(0,-1)]:
                newr , newc = r + i, c + j
                if 0 <= newr < n and 0 <= newc < n and grid[newr][newc] == 1:
                    rt += dfs(newr,newc)
            return rt
        def dfs2(r,c,v):
            nonlocal grid
            if grid[r][c] != -1:
                return
            grid[r][c] = 0
            dm[(r,c)] = v
            for i , j in [(1,0),(-1,0),(0,1),(0,-1)]:
                newr , newc = r + i, c + j
                if 0 <= newr < n and 0 <= newc < n and grid[newr][newc] == -1:
                    dfs2(newr,newc,v)
            return
        ans = 0; idx = 0
        for i in range(n):
            for j in range(n):
                area = dfs(i,j) if grid[i][j] == 1 else 0
                ans = max(ans,area)
                dfs2(i,j,(idx,area))
                idx += 1

        def cnt(r,c):
            if 0 <= r < n and 0 <= c < n:
                return dm[(r,c)] if dm[(r,c)] else (-1,0)
            return (-1,0)
        
        for i in range(n):
            for j in range(n):
                if original[i][j] == 0:
                    m_set = set()
                    for i1 , j1 in [(1,0),(-1,0),(0,1),(0,-1)]:
                        newi , newj = i + i1, j+ j1
                        m_set.add(cnt(newi,newj))
                    new_area = 1
                    for k in m_set:
                        new_area += k[1]
                    ans = max(ans,new_area)
        return ans
        