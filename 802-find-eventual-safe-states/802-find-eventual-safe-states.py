class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse_graph = [[] for _ in range(len(graph))]
        indegree = [0] * len(graph)
        queue = []
        for index,item in enumerate(graph):
            for j in item:
                reverse_graph[j].append(index)
            indegree[index] = len(item)
            if len(item) == 0:
                queue.append(index)
        while queue != []:
            index = queue.pop(0)
            for i in reverse_graph[index]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return [index for index,item in enumerate(indegree) if item == 0]
        # print(reverse_graph)
        # print(indegree)

        
        