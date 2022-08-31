class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights) ; n = len(heights[0])
        table = collections.defaultdict(set)
        path = set()
        def dfs(row,col,status):
            path.add((row,col))
            if status not in table[(row,col)]:
                table[(row,col)].add(status)
                for i , j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    newrow = row + i ; newcol = col + j
                    if 0 <= newrow < m and 0 <= newcol < n and heights[row][col]<= heights[newrow][newcol] and (newrow,newcol) not in path:
                        dfs(newrow,newcol,status)
            path.remove((row,col))
            return
                    
        for i in range(m):
            dfs(i,0,"P")
            dfs(i,n-1,"A")
        for i in range(n):
            dfs(0,i,"P")
            dfs(m-1,i,"A")
        ans = []
        for i in table:
            if len(table[i]) == 2:
                ans.append([i[0],i[1]])
        return ans
        