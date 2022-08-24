class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        table = {}
        m = len(grid) ; n = len(grid[0])
        def bfs(row,col):
            return __bfs(row,col,"R") + __bfs(row,col,"L") + __bfs(row,col,"D") + __bfs(row,col,"U")
        
        def __bfs(row,col,direction):
            if (row,col,direction) in table:
                return table[(row,col,direction)]
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == "W":
                return 0
            if direction == "R":
                newrow = row ; newcol = col + 1
            elif direction == "L":
                newrow = row ; newcol = col - 1
            elif direction == "U":
                newrow  = row - 1 ; newcol = col
            else:
                newrow = row + 1 ; newcol = col
            if grid[row][col] == "E":
                table[(row,col,direction)] = 1 + __bfs(newrow,newcol,direction)
                return table[(row,col,direction)] 
            else:
                table[(row,col,direction)] = __bfs(newrow,newcol,direction)
                return table[(row,col,direction)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    ans = max(ans,bfs(i,j))
        return ans
                
                
        