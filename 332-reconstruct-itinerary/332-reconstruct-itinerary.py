class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for index  , (start , end) in enumerate(tickets):
            if start not in graph:
                graph[start] = []
            graph[start].append((end,index))
        for i in graph:
            graph[i].sort()
        visited = [False for _ in range(len(tickets))]
        start = "JFK"
        ans = None
        def backtracking(start,path):
            nonlocal ans
            if ans != None:
                return
            if all(visited):
                ans = path[:]
                return
            if start not in graph:
                return
            for end , index in graph[start]:
                if visited[index] == True:
                    continue
                visited[index] = True
                path.append(end)
                backtracking(end,path)
                visited[index] = False
                path.pop()
        backtracking("JFK",["JFK"])
        return ans
        