class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(set)
        for u , v in edges:
            adj[u].add(v)
            adj[v].add(u)
        q = []
        for i in adj:
            if len(adj[i]) == 1:
                q.append(i)
        prev = [i for i in range(n)]
        while q:
            prev = q.copy()
            length = len(q)
            for _ in range(length):
                leaf = q.pop(0)
                if len(adj[leaf]) == 0:
                    continue
                mother = list(adj[leaf])[0]
                adj[leaf].remove(mother)
                adj[mother].remove(leaf)
                if len(adj[mother]) == 1:
                    q.append(mother)
        return prev
