class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        directions = [(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2)]
        queue = [(0,0)]
        visited = set() ; visited.add((0,0))
        step = 0
        while queue != []:
            length = len(queue)
            for _ in range(length):
                row , col = queue.pop(0)
                if row == x and col == y:
                    return step
                for i , j in directions:
                    newRow = row + i ; newCol = col + j
                    if (newRow,newCol) not in visited:
                        queue.append((newRow,newCol))
                        visited.add((newRow,newCol))
            step += 1
        return
        