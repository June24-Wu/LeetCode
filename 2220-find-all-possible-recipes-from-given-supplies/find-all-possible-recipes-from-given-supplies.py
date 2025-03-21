class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = collections.defaultdict(set)
        in_count = collections.defaultdict(int) 
        n = len(recipes)
        for i in range(n):
            u = recipes[i]
            for v in ingredients[i]:
                adj[v].add(u)
                in_count[u] += 1
        ans = set()
        def dfs(node):
            nonlocal ans
            if in_count[node] == 0 and node in recipes:
                ans.add(node)
            for t in adj[node]:
                in_count[t] -= 1
                if in_count[t] == 0:
                    dfs(t)
            return
        
        for i in supplies:
            dfs(i)
        return list(ans)
        # def dfs(node):
        #     if in_count[node]
        