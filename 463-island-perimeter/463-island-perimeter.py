class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid) ; n = len(grid[0])
        
        def isLake(row,col):
            if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                return False
            return True
            
        for i in range(m):
            for j in range(n):
                if not isLake(i,j):
                    for x , y in [(0,1),(0,-1),(1,0),(-1,0)]:
                        if isLake(i+x,j+y):
                            ans += 1
                # print(i,j,ans)
        return ans
        