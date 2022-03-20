class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for _ in range(n)] for _ in range(n)]
        up , down , left , right = 0, n-1,0,n-1
        num = 1
        while left <= right and up <= down:
            for i in range(left,right):
                matrix[up][i] = num
                num += 1
            for i in range(up,down):
                matrix[i][right] = num
                num += 1
            for i in range(right,left,-1):
                matrix[down][i] = num
                num += 1
            for i in range(down,up,-1):
                matrix[i][left] = num
                num += 1
            left +=1
            right -=1
            up +=1
            down -=1
        if n%2 ==1:
            matrix[n//2][n//2] = num
        return matrix