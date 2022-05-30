class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        queue = [(start[0],start[1])]
        visited = set()
        m = len(maze) ; n = len(maze[0])
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        while queue != []:
            curr = queue.pop()
            if [curr[0],curr[1]] == destination:
                return True
            for i , j in directions:
                x = curr[0] ; y = curr[1]
                while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                    x += i ; y +=j
                x -= i ; y -= j
                if (x,y) not in visited:
                    queue.append((x,y))
                    visited.add((x,y))
        return False
                