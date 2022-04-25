class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix) ; n = len(matrix[0])
        def get(row,col):
            if row < 0 or row>= m or col < 0 or col >= n :
                return float("inf")
            return matrix[row][col]
        if m == 1: return min(matrix[0])
        for i in range(m-2,-1,-1):
            for j in range(n):
                matrix[i][j] = matrix[i][j] + min(get(i+1,j-1),get(i+1,j),get(i+1,j+1))
        # print(matrix)
        return min(matrix[0])
        