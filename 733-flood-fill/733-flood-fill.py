class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image) ; n = len(image[0])
        old = image[sr][sc]
        visited = [[False for _ in range(n)]for _ in range(m)]
        def dfs(row,col):
            if row<0 or row >= m or col < 0 or col >= n:
                return
            if image[row][col] != old:
                return
            if visited[row][col] == True:
                return
            image[row][col] = newColor
            visited[row][col] = True
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col-1)
            dfs(row,col+1)
            return
        dfs(sr,sc)
        return image
        