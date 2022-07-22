class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(set)
        for s , e in edges:
            graph[s].add(e)
        visited = [False for _ in range(n)]
        flag = None
        print(graph)
        def dfs(node,visited):
            nonlocal flag
            if flag == False:
                return
            if visited[node] == True:
                # print(node,visited)
                flag = False
                return
            if graph[node] == set():
                if node == destination:
                    flag = True
                else:
                    # print("step2",node,visited)
                    flag = False
                return
            visited[node] = True
            for to in graph[node]:
                dfs(to,visited)
            visited[node] = False
            return
        dfs(source,visited)
        # print(flag)
        if flag == True:
            return True
        return False
            
        