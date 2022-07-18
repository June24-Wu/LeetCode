class NumMatrix:

    def __init__(self, mat: List[List[int]]):
        m = len(mat) ; n = len(mat[0])
        preSum = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    preSum[i][j] = mat[i][j]
                elif i == 0:
                    preSum[i][j] = preSum[i][j-1] +  mat[i][j]
                elif j == 0:
                    preSum[i][j] = preSum[i-1][j] +  mat[i][j]                    
                    
                else:
                    preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1] + mat[i][j]
        self.preSum = preSum
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.preSum[row2][col2]
        elif row1 == 0:
            return self.preSum[row2][col2] - self.preSum[row2][col1-1]
        elif col1 == 0:
            return self.preSum[row2][col2] - self.preSum[row1-1][col2]
        else:
            return self.preSum[row2][col2] - self.preSum[row2][col1-1] - self.preSum[row1-1][col2] + self.preSum[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)