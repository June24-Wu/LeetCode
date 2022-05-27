class Solution(object):
    def swimInWater(self, heights):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(heights) ; n = len(heights[0])
        pq = [(heights[0][0],0,0)]
        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        visited = set()
        dp[0][0] = heights[0][0]
        while pq != []:
            height , row , col = heapq.heappop(pq)
            visited.add((row,col))
            for i , j in [(0,1),(0,-1),(1,0),(-1,0)]:
                newRow = row + i ; newCol = col + j
                if 0 <= newRow < m and 0 <= newCol < n and (newRow,newCol) not in visited:
                    newHeight = heights[newRow][newCol]
                    maxHeight = max(newHeight,dp[row][col])
                    if maxHeight < dp[newRow][newCol]:
                        heapq.heappush(pq,(maxHeight,newRow,newCol))
                        dp[newRow][newCol] = maxHeight
        #     print(pq)
        # print(dp)
        return dp[-1][-1]
        