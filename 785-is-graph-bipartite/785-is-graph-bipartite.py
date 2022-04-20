class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False for _ in range(len(graph))]
        res = True
        def dfs(num,color):
            
            nonlocal res ; nonlocal visited
            if res == False:return
            if visited[num] == False:
                visited[num] = color
                for i in graph[num]:
                    new_color = 2 if color == 1 else 1
                    dfs(i,new_color)
            else:
                if visited[num] != color:
                    res = False
                return

        for i in range(len(graph)):
            if visited[i] == False:
                dfs(i,1)
        return res
        
        