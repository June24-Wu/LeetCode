class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for row in matrix:
            if target < row[0]:
                return False
            if target > row[n-1]:
                continue
            for val in row:
                if val == target:
                    return True
                else:
                    continue
        return False
            
        