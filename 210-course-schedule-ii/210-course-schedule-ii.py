class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for i in range(numCourses)]
        for i in prerequisites:
            indegree[i[0]] += 1
            graph[i[1]].append(i[0])
        # BFS
        # initialize queue
        queue = [] ; res = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                res.append(i)
        cnt = 0 
        while queue != []:
            cur = queue.pop(0)
            cnt += 1
            for i in graph[cur]: # i means child
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
                    res.append(i)
        if cnt == len(graph):
            return res
        return []
      
            
        # DFS
        # visted = [False for _ in range(len(graph))]
        # path = [False for _ in range(len(graph))]
        # hasCycle = False
        # res = []
        # def dfs(num):
        #     nonlocal visted ; nonlocal path ; nonlocal hasCycle ; nonlocal res
        #     if path[num] == True:
        #         hasCycle = True
        #         return
        #     if hasCycle or visted[num]:
        #         return
        #     visted[num] = True ; path[num] = True
        #     for i in graph[num]:
        #         dfs(i)
        #     res.append(num)
        #     path[num] = False
        #     return
        # for i in range(len(graph)):
        #     dfs(i)
        # if hasCycle:return []
        # return res[::-1]

        