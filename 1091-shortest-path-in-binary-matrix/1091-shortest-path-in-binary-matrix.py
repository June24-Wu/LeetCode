class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = [(0,0)]
        m = len(grid) ; n = len(grid[0])
        visited = set() ; visited.add((0,0))
        if grid[0][0] == 1:
            return -1
        cnt = 1
        while queue:
            length = len(queue)
            for _ in range(length):
                r , c = queue.pop(0)
                if r == m - 1 and c == n- 1:
                    return cnt
                for (i,j) in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]:
                    row = r + i ; col = c + j
                    if 0 <= row < m and 0 <= col < n and (row,col) not in visited and grid[row][col] == 0:
                        queue.append((row,col))
                        visited.add((row,col))
            cnt += 1
        return -1
        