class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * n
        graph = collections.defaultdict(list)
        indegree = [0] * n
        for i , j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        queue = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.pop(0)
            visited[node] = True
            for next in graph[node]:
                if visited[next]:
                    return False
                indegree[next] -= 1
                if indegree[next] == 0:
                    queue.append(next)
        
        return max(indegree) == 0
        
        
        
        
        # DFS
        # visited = [False] * n
        # path = [False] * n
        # graph = collections.defaultdict(list)
        # for i , j in prerequisites:
        #     if j not in graph:
        #         graph[j] = []
        #     graph[j].append(i)
        # flag = True
        # print(graph)
        # def dfs(index):
        #     nonlocal flag ; nonlocal path ; nonlocal visited
        #     if path[index]:
        #         flag = False
        #         return
        #     if visited[index] or flag == False:
        #         return
        #     visited[index] = True
        #     path[index] = True
        #     for next in graph[index]:
        #         dfs(next)
        #     path[index] = False
        #     return
        # for i in range(n):
        #     dfs(i)
        # return flag
        