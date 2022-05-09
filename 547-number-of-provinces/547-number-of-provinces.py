class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        length = len(isConnected)
        visited = [False for _ in range(length)]
        
        def dfs(index):
            nonlocal visited
            if visited[index] == True:
                return
            visited[index] = True
            for i in range(len(isConnected[index])):
                if i != index and isConnected[index][i] == 1:
                    dfs(i)
            return
        
        
        cnt = 0
        for i in range(len(isConnected)):
            if visited[i] == False:
                dfs(i)
                cnt += 1
        return cnt
            
        