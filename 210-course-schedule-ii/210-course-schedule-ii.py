class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(n)]
        graph = collections.defaultdict(list)
        for i , j in prerequisites:
            indegree[i] += 1
            graph[j].append(i)
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        ans = []
        while queue:
            node = queue.pop(0)
            ans.append(node)
            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        if max(indegree) > 0 :
            return []
        return ans
        
            
        