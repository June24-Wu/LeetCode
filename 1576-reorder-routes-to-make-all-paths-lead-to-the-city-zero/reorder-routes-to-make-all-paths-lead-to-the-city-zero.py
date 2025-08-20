class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = collections.defaultdict(dict)
        for u , v in connections:
            if "to" not in adj[u]:
                adj[u]["to"] = set()
            if "from" not in adj[u]:
                adj[u]["from"] = set()
            adj[u]["to"].add(v)
            if "from" not in adj[v]:
                adj[v]["from"] = set()
            if "to" not in adj[v]:
                adj[v]["to"] = set()
            adj[v]["from"].add(u)
        vis = set()
        ans = 0
        def dfs(idx,pre):
            nonlocal vis
            nonlocal ans
            if idx in vis:
                return
            vis.add(idx)
            for i in adj[idx]["to"]:
                if i != pre:
                    ans += 1
                dfs(i,idx)
            for i in adj[idx]["from"]:
                dfs(i,idx)
            return
        dfs(0,-1)     
        
        return ans
