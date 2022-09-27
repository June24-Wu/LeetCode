class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix) ; n = len(matrix[0])
        def get(row,col):
            if 0 <= row < m and 0<= col < n:
                return matrix[row][col]
            return 0
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(get(i-1,j),get(i,j-1),get(i-1,j-1)) + 1
                    ans += matrix[i][j]
        return ans