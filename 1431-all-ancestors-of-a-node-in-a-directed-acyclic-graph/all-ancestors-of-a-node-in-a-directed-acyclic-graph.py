class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        inlist = [0 for _ in range(n)]
        adj = collections.defaultdict(set)
        for u , v in edges:
            adj[u].add(v)
            inlist[v] += 1
        q = []
        for i in range(n):
            if inlist[i] == 0:
                q.append(i)
        while q:
            node = q.pop(0)
            for child in adj[node]:
                ans[child] = ans[child].union(ans[node])
                ans[child].add(node)
                inlist[child] -= 1
                if inlist[child] == 0:
                    q.append(child)
        ans = [sorted(list(i)) for i in ans]
        return ans
        