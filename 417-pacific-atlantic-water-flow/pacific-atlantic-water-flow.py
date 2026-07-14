class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m1 = set(); m2 = set()
        m = len(heights); n = len(heights[0])

        def dfs(r,c,vis):
            if (r,c) in vis:
                return
            vis.add((r,c))
            for i , j in [(1,0),(-1,0),(0,1),(0,-1)]:
                newr, newc = r + i, c + j 
                if 0 <= newr < m and 0 <= newc < n and heights[newr][newc] >= heights[r][c]:
                    dfs(newr,newc,vis)
            return
        for i in range(m):
            dfs(i,0,m1)
            dfs(i,n-1,m2)
        for i in range(n):
            dfs(0,i,m1)
            dfs(m-1,i,m2)
        ans = []
        # print(m1)
        # print(m2)
        for i in m1:
            # print(i)
            if i in m2:
                ans.append([i[0],i[1]])
        return sorted(ans)

        