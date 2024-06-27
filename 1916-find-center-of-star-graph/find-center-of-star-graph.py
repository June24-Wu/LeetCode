class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(set)
        for u ,v in edges:
            adj[u].add(v)
            adj[v].add(u)
        for i in adj:
            if len(adj[i]) == len(edges):
                return i
        print(adj)
        