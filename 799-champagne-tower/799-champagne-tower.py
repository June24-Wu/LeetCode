class Solution:
    def champagneTower(self, poured: int, r: int, c: int) -> float:
        dp = [[0 for _ in range(101)] for _ in range(101)]
        m = len(dp) ; n = len(dp[0])
        dp[0][0] = poured
        
        
        def get(row,col):
            if 0 <= row < m and 0 <= col < n:
                return max(0,float(dp[row][col] - 1)) / 2
            return float(0)
        for row in range(1,len(dp)):
            if max(dp[row-1]) == 0:
                break
            for col in range(len(dp[row])):
                dp[row][col] = get(row-1,col) + get(row-1,col-1)
        # print(dp)
        return min(1,dp[r][c])
        