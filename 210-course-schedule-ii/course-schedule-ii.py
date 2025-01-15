class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        inc = [0 for _ in range(n)]
        adj = collections.defaultdict(set)
        for u , v in prerequisites:
            adj[v].add(u)
            inc[u] += 1
        ans = []
        def dfs(idx):
            if inc[idx] == 0:
                ans.append(idx)
            for i in adj[idx]:
                inc[i] -= 1
                if inc[i] == 0:
                    dfs(i)
            return
        for i in range(n):
            if inc[i] == 0 and i not in ans:
                dfs(i)
        return ans if len(ans) == n else []

        