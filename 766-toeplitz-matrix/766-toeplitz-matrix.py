class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        def isToeplitzVal(m,n):
            val = matrix[m][n]
            while m < row and n < column:
                if matrix[m][n] != val:
                    return False
                m += 1
                n += 1
            return True
        for i in range(column):
            if isToeplitzVal(0,i) == False:
                return False
        for i in range(row):
            if isToeplitzVal(i,0) == False:
                return False
        return True
            
            
        