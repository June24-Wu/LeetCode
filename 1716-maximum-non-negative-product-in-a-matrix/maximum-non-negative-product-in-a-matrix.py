class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        ans = - float("inf")
        m = len(grid); n = len(grid[0])
        
        @cache
        def bt(row,col,curr):
            nonlocal ans
            # print(row,col,curr,grid[row][col])
            if grid[row][col] == 0:
                ans = max(0,ans)
                return
            curr = curr * grid[row][col]
            if row == m - 1 and col == n - 1:
                ans = max(ans,curr)
                return
            if row + 1 < m: 
                bt(row+1,col,curr)
            if col + 1 < n:
                bt(row,col+1,curr)
            return
        bt(0,0,1)
        return int(ans % (1e9 + 7)) if ans >= 0 else -1
            
            
        