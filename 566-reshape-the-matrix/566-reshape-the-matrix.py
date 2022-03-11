class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if c*r != len(mat) * len(mat[0]):
            return mat
        newMat = [[0 for i in range(c)] for _ in range(r)]
        column = 0
        row = 0
        for i in mat:
            for j in i:
                if column == c:
                    column = 0
                    row += 1
                newMat[row][column] = j 
                column += 1
        return newMat
        