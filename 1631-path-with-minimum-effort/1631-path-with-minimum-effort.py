class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        # Variations of Dijkstra's Algorithm
        
        m = len(heights) ; n = len(heights[0])
        pq = [(0,0,0)]
        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        visited = set()
        dp[0][0] = 0
        while pq != []:
            diff , row , col = heapq.heappop(pq)
            visited.add((row,col))
            for i , j in [(0,1),(0,-1),(1,0),(-1,0)]:
                newRow = row + i ; newCol = col + j
                if 0 <= newRow < m and 0 <= newCol < n and (newRow,newCol) not in visited:
                    newDiff = abs(heights[newRow][newCol] - heights[row][col])
                    maxDiff = max(newDiff,dp[row][col])
                    if maxDiff < dp[newRow][newCol]:
                        heapq.heappush(pq,(maxDiff,newRow,newCol))
                        dp[newRow][newCol] = maxDiff
        return dp[-1][-1]
                    
                    
                    