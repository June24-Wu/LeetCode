class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = [(0,0,0)]
        m = len(grid) ; n = len(grid[0])
        step = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        while queue != []:
            length = len(queue)
            for _ in range(length):
                row , col , numOfRemoveK = queue.pop(0)
                if row == m - 1 and col == n - 1:
                    return step
                for i , j in directions:
                    newRow = row + i ; newCol = col + j
                    if 0 <= newRow < m and 0<= newCol < n:
                        numOfRemoveKNew = numOfRemoveK + grid[newRow][newCol]
                        if numOfRemoveKNew <= k and (newRow,newCol,numOfRemoveKNew) not in visited:
                            queue.append((newRow,newCol,numOfRemoveKNew))
                            visited.add((newRow,newCol,numOfRemoveKNew))
            step += 1
        return -1
                        
                        
                
        