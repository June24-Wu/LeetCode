class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid) ; n = len(grid[0])
        visited = set() ; visited.add((0,0))
        if grid[0][0] == 1:
            return -1
        queue = [(0,0)]
        step = 1
        directions = [(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,0),(-1,1),(-1,-1)]
        while queue != []:
            length = len(queue)
            for _ in range(length):
                row , col = queue.pop(0)
                if row == m - 1 and col == n - 1:
                    return step
                for i , j in directions:
                    newRow = row + i ; newCol = col + j
                    if 0<= newRow < m and 0 <= newCol < n and (newRow,newCol) not in visited and grid[newRow][newCol] == 0:
                        queue.append((newRow,newCol))
                        visited.add((newRow,newCol))
            step += 1
        return -1