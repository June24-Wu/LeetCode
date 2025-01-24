class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = collections.defaultdict(set)
        in_count = [0 for _ in range(n)]
        for u , vs in enumerate(graph):
            for v in vs:
                adj[v].add(u)
                in_count[u] += 1
        q = []
        ans = []
        for i in range(n):
            if in_count[i] == 0:
                q.append(i)
        while q:
            length = len(q)
            for _ in range(length):
                node = q.pop(0)
                ans.append(node)
                for child in adj[node]:
                    in_count[child] -= 1
                    if in_count[child] == 0:
                        q.append(child)
        ans.sort()
        return ans
        