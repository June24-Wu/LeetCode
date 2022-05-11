class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False for _ in range(n)]
        
        def dfs(index):
            if visited[index] == True:
                return
            keys = rooms[index]
            visited[index] = True
            for i in keys:
                dfs(i)
            return
        dfs(0)
        return all(visited) == True
            
        