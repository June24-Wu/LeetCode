class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [i for i in range(n)]
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        def union(a,b):
            a = find(a)
            b = find(b)
            parents[b] = a
        for u , v in edges:
            union(u,v)
        return find(source) == find(destination)