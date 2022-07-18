class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat) ; n = len(mat[0])
        preSum = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    preSum[i][j] = mat[i][j]
                elif i == 0 :
                    preSum[i][j] = preSum[i][j-1] + mat[i][j]
                elif j == 0 :
                    preSum[i][j] = preSum[i-1][j] + mat[i][j]
                else:
                    preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1] + mat[i][j]
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x0 = max(i-k,0) ; x1 = min(i+k,m-1) ; y0 = max(j-k,0) ; y1 = min(j+k,n-1)
                if x0 == 0 and y0 == 0:
                    ans[i][j] = preSum[x1][y1]
                elif x0 == 0:
                    ans[i][j] = preSum[x1][y1] - preSum[x1][y0-1]
                elif y0 == 0:
                    ans[i][j] = preSum[x1][y1] - preSum[x0-1][y1]
                else:
                    ans[i][j] = preSum[x1][y1] - preSum[x1][y0-1] - preSum[x0-1][y1] + preSum[x0-1][y0-1]
        return ans
                    
        