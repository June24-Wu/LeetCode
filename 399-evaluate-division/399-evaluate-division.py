class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # 构建有向图
        table = collections.defaultdict(dict)
        for (x,y) , val in zip(equations,values):
            table[x][y] = val
            table[y][x] = 1 / val
        
        
        def dfs(x,y,visited):
            if x not in table or y not in table:
                return -1
            if x == y:
                return 1
            visited.add(x)
            for i in table[x]:
                if i not in visited:
                    Val = dfs(i,y,visited)
                    if Val >=0:
                        return Val * table[x][i]
            return -1
        
        ans = []
        for x , y in queries:
            ans.append(dfs(x,y,set()))
        return ans
            
                    
            
        