class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        res = []
        def dfs(index,path):
            nonlocal res
            path.append(index)
            if index == end:
                res.append(path[:])
            for i in graph[index]:
                dfs(i,path)
            path.pop()
            return
        dfs(0,[])
        return res
            
        