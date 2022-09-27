class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m = len(grid) ; n = len(grid[0])
        updown = [[[0,0] for _ in range(n)] for _ in range(m)]
        bottomup = [[[0,0] for _ in range(n)] for _ in range(m)]
        
        def get(dp,row,col,status):
            if 0 <= row < m and 0<= col < n:
                return dp[row][col][status]
            return 0
        def getGrid(row,col):
            if 0 <= row < m and 0<= col < n:
                return grid[row][col]
            return None
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "W":
                    updown[i][j][0] += get(updown,i,j-1,0) + (getGrid(i,j-1) == "E")
                    updown[i][j][1] += get(updown,i-1,j,1) + (getGrid(i-1,j) == "E")
                    
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j] != "W":
                    bottomup[i][j][0] += get(bottomup,i,j+1,0) + (getGrid(i,j+1) == "E")
                    bottomup[i][j][1] += get(bottomup,i+1,j,1) + (getGrid(i+1,j) == "E")

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j] == "0":
                    ans = max(ans,sum(bottomup[i][j]) + sum(updown[i][j]))
        # print(dp)
        return ans
                
        