class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [float("inf")] * (n+1)
        
        for i in range(m - 1, -1, -1):
            temp = dp.copy()
            dp = [float("inf")] * (n+1)
            for j in range(n - 1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[j] = max(1- dungeon[i][j], 1)
                    continue
                minn = min(temp[j], dp[j + 1])
                dp[j] = max(minn - dungeon[i][j], 1)
            # print(dp)
        return dp[0]