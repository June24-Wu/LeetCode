class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i , j = 0 , 0
        m = len(mat) ; n = len(mat[0])
        ans = []
        flag = True
        
        def downToUp(i,j,mat):
            nonlocal n
            temp = []
            while i >= 0  and j <= n - 1:
                temp.append(mat[i][j])
                i -= 1
                j += 1
            return temp
        def upToDown(i,j,mat):
            nonlocal n
            temp = []
            while i >= 0  and j <= n - 1:
                temp.insert(0,mat[i][j])
                i -= 1
                j += 1
            return temp
        
        while i <= m- 1 and j <= n-1:
            if flag == True:
                ans.extend(downToUp(i,j,mat))
            else:
                ans.extend(upToDown(i,j,mat))
            if i != m - 1:
                i+= 1
            else:
                j += 1
            flag = not flag
        return ans
            
                
        
        
        
        
              
        