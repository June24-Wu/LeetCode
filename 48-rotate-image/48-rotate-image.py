class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        left = 0 ; right = n - 1
        while left < right:
            for i in range(n):
                matrix[i][left] , matrix[i][right] = matrix[i][right] , matrix[i][left]
            left += 1;  right -= 1
        return
        