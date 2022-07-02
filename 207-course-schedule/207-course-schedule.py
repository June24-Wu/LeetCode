class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * n
        path = [False] * n
        graph = collections.defaultdict(list)
        for i , j in prerequisites:
            if j not in graph:
                graph[j] = []
            graph[j].append(i)
        flag = True
        print(graph)
        def dfs(index):
            nonlocal flag ; nonlocal path ; nonlocal visited
            if path[index]:
                flag = False
                return
            if visited[index] or flag == False:
                return
            visited[index] = True
            path[index] = True
            for next in graph[index]:
                dfs(next)
            path[index] = False
            return
        for i in range(n):
            dfs(i)
        return flag
        