class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        locations = []
        m = len(matrix) ; n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    locations.append((i,j))
        for r , c in locations:
            for i in range(m):
                matrix[i][c] = 0
            for i in range(n):
                matrix[r][i] = 0
                
        