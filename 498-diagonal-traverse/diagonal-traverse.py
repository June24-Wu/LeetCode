class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        res = []
        n, m = len(mat), len(mat[0])

        x,y = 0, 0
        vX, vY = -1, 1
        while len(res) < n*m:
            #print(x,y, res)
            if 0 <= x < n and 0<= y < m:
                res.append(mat[x][y])
                x += vX
                y += vY
            elif x == -1 and 0<= y < m : #hit the -1 row
                x = 0
                vX, vY = 1, -1
            elif 0 <= x < n and y == -1: # hit the -1 column
                y = 0
                vX, vY = -1, 1
            elif y == m: # hit outright column
                y = m-1
                x += 2
                vX, vY = 1, -1
            elif x == n: # hit bottom row
                y += 2
                x = n-1
                vX, vY = -1, 1
        return res