class Solution:
    def maxPoints(self, p: List[List[int]]) -> int:
        m = len(p) ; n = len(p[0])
        dp = p[0].copy()
        left = [0] * n ; right = [0] * n
        for r in range(1,m):
            for c in range(n):
                left[c] = dp[c] if c == 0 else max(dp[c],left[c-1] - 1)
            for c in range(n-1,-1,-1):
                right[c] = dp[c] if c == n - 1 else max(dp[c],right[c+1] -  1)
            for c in range(n):
                dp[c] = p[r][c] + max(left[c] , right[c])
        return max(dp)
        
        
        
        
        # TLE O(m * n * n)
        m = len(p) ; n = len(p[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = p[0].copy()
        for r in range(1,m):
            for c in range(n):
                for c2 in range(n):
                    dp[r][c] = max(dp[r][c],dp[r-1][c2] + p[r][c] - abs(c-c2))
        # print(dp)
        return max(dp[-1])
        