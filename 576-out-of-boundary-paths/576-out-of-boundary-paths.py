class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        
        def dfs(r,c,step):
            nonlocal memo
            if (r,c,step) in memo:
                return memo[(r,c,step)]
            if step == 0:
                if 0 <= r < m and 0 <= c < n:
                    return 0
                return 1
            num = 0
            for (i,j) in [(1,0),(-1,0),(0,1),(0,-1)]:
                row = r +i ; col = c + j
                if 0 <= row < m and 0<= col < n:
                    num += dfs(row,col,step - 1)
                else:
                    num += 1
            memo[(r,c,step)] = num
            return num
        return dfs(startRow,startColumn,maxMove) % (10**9+7)
                
        