class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n-1,-1,-1):
            r = i; c = 0; curr = []
            while r < n and c < n:
                curr.append(grid[r][c])
                r+=1;c+=1
            curr.sort(reverse=True)
            r = i; c = 0
            while r < n and c < n:
                grid[r][c] = curr.pop(0)
                r += 1; c+= 1
        for i in range(1,n):
            r = 0; c = i; curr = []
            while r < n and c < n:
                curr.append(grid[r][c])
                r+=1;c+=1
            curr.sort()
            r = 0
            c = i
            while r < n and c < n:
                grid[r][c] = curr.pop(0)
                r += 1; c+= 1
        return grid
        