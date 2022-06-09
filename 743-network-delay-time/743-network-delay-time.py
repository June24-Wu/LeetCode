class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = [float("inf") for _ in range(n)]
        graph = [[float("inf") for _ in range(n)] for _ in range(n)]
        for start , end , val in times:
            graph[start-1][end-1] = val
        k -= 1 
        queue = [(0,k)] ; visited[k] = 0
        while queue:
            # print(queue)
            # print(visited)
            if max(visited) != float("inf"):
                return max(visited)
            val , node = heapq.heappop(queue)
            visited[node] = min(val,visited[node])
            for end in range(n):
                if graph[node][end] != float("inf") and visited[end] == float("inf"):
                    heapq.heappush(queue,(val + graph[node][end],end))
        if max(visited) != float("inf"):
            return max(visited)        
        return -1