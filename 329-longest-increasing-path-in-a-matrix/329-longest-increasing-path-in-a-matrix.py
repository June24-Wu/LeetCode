class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirn = [(-1,0),(1,0),(0,-1),(0,1)]
        def explore(i,j,graph,visited,prev,dp):
            if i >= len(graph) or i < 0 or j >= len(graph[0]) or j < 0 or graph[i][j] <= prev or visited[i][j]:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            visited[i][j] = True
            maxe = 1
            for dx,dy in dirn:
                nx = i+dx
                ny = j+dy
                maxe = max(explore(nx,ny,graph,visited,graph[i][j],dp)+1,maxe)
            dp[i][j] = maxe
            visited[i][j] = False
            return maxe
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        ans = 0
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans,explore(i,j,matrix,visited,float("-inf"),dp))
        return ans
        
        
        
                    
        