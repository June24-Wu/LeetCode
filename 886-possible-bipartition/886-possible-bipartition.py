class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for i in range(n)]
        for i in dislikes:
            graph[i[0]-1].append(i[1]-1)
            graph[i[1]-1].append(i[0]-1)
        visited = [False for _ in range(n)]
        flag = True
        def dfs(index,color):
            nonlocal flag
            nonlocal visited
            if flag == False:return
            if visited[index] != False:
                if color != visited[index]:
                    flag = False
                return    
            # if visited[index] == False:
            visited[index] = color
            newColor = 1 if color == 2 else 2
            for i in graph[index]:
                dfs(i,newColor)
            return
        for i in range(len(graph)):
            if visited[i] == False:
                dfs(i,1)
        # print(flag)    
        # print(graph)
        # print(visited)
        return flag
        