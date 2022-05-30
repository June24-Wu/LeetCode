class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        ROWS, COLS = len(maze), len(maze[0])
        hr, hc = hole
        path, pq = dict(), [[0, '', ball[0], ball[1]]]

        def move_col(r, c, inc):
            while 0 <= c + inc < COLS and maze[r][c + inc] == 0:
                if (r, c) == (hr, hc):
                    break
                c += inc
            return c

        def move_row(r, c, inc):
            while 0 <= r + inc < ROWS and maze[r + inc][c] == 0:
                if (r, c) == (hr, hc):
                    break
                r += inc
            return r

        while pq:
            length, p, row, col = heappop(pq)
            key = (row, col)
            if key not in path:

                path[key] = (length, p)

                c = move_col(row, col, -1)
                if c != col: heappush(pq, (length + abs(c - col), p + 'l', row, c))

                c = move_col(row, col, 1)
                if c != col: heappush(pq, (length + abs(c - col), p + 'r', row, c))

                r = move_row(row, col, -1)
                if r != row: heappush(pq, (length + abs(r - row), p + 'u', r, col))

                r = move_row(row, col, 1)
                if r != row: heappush(pq, (length + abs(r - row), p + 'd', r, col))

        if (hr, hc) not in path: return 'impossible'
        return path[(hr, hc)][1]