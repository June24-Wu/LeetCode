class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater) ; n = len(isWater[0])
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        q = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    ans[i][j] = 0
                    q.append([i,j])
        while q:
            length = len(q)
            for _ in range(length):
                r , c = q.pop(0)
                for i , j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    newr , newc = r + i , c + j
                    if 0 <= newr < m and 0 <= newc < n and ans[newr][newc] == -1:
                        ans[newr][newc] = ans[r][c] + 1
                        q.append([newr,newc])
        return ans
        