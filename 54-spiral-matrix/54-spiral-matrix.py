class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        num = 1
        up,down,left,right = 0,m-1,0,n-1
        new = []
        numEle = m * n 
        while numEle >= 1:
            for i in range(left,right+1):
                if numEle >= 1:
                    new.append(matrix[up][i])
                    numEle -=1
            up +=1
            
            for i in range(up,down+1):
                if numEle >= 1:
                    new.append(matrix[i][right])
                    numEle -=1
            right -=1
            
            for i in range(right,left-1,-1):
                if numEle >= 1:
                    new.append(matrix[down][i])
                    numEle -=1
            down -=1
                
            for i in range(down,up-1,-1):
                if numEle >= 1:
                    new.append(matrix[i][left])
                    numEle -=1
            left +=1

        return new