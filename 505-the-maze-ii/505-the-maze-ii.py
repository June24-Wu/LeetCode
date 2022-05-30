class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze) ; n = len(maze[0])
        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        dp[start[0]][start[1]] = 0
        pq = [(0,start[0],start[1])]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while pq:
            distance , x , y = heapq.heappop(pq)
            for i , j in directions:
                count = 0 ; row = x ; col = y
                while 0 <= row < m and 0 <= col < n and maze[row][col] == 0:
                    row += i ; col += j ; count += 1
                row -= i ; col -= j ; count -= 1
                if distance + count < dp[row][col]:
                    dp[row][col] = distance + count
                    heapq.heappush(pq,(distance+count,row,col))
        return -1 if dp[destination[0]][destination[1]] == float("inf") else dp[destination[0]][destination[1]]
        