class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        m = len(grid) ; n = len(grid[0])
        table = {0:0} # index : area
        
        def dfs(row,col,markedIndex):
            nonlocal grid
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0
            if grid[row][col] != 1:
                return 0
            grid[row][col] = markedIndex
            area = dfs(row-1,col,index) + dfs(row+1,col,index) + dfs(row,col-1,index) + dfs(row,col+1,index) + 1
            self.maxArea = max(area,self.maxArea)
            return area
        
        
        def get(i,j):
            if i < 0 or i >=m or j < 0 or j >=n:
                return 0 
            return grid[i][j]
        index = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i,j,index)
                    table[index] = area
                    index += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    area = 1
                    indexList = []
                    for t , k in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if get(t,k) not in indexList:
                            area += table[get(t,k)]
                            indexList.append(get(t,k))
                    self.maxArea = max(area,self.maxArea)
        # print(grid)
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 0:
        #             temp = copy.deepcopy(grid)
        #             temp[i][j] = 1
        #             dfs(i,j)
        return self.maxArea
        