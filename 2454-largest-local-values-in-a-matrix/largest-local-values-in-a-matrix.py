class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid) ; n = len(grid[0])
        ans = [[ - float("inf") for _ in range(n-2)] for _ in range(m-2)]
        for i in range(m-2):
            for j in range(n-2):
                up = i ; down = up + 3 ; left = j ; right = left + 3
                maxval =  - float("inf")
                for r in range(up,down):
                    for c in range(left,right):
                        maxval = max(maxval,grid[r][c])
                ans[i][j] = maxval
        return ans
        