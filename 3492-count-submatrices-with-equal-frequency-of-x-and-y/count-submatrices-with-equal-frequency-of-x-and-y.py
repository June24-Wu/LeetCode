class Calculator:
    def __init__(self,x,y,dot):
        self.x = x
        self.y = y
        self.dot = dot
    def is_valid(self):
        return self.x == self.y and self.x > 0

    def __str__(self):
        return f"{self.x},{self.y},{self.dot}"

    def __repr__(self):
        return f"{self.x},{self.y},{self.dot}"

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid); n = len(grid[0])

        dp = [[None for _ in range(n)] for _ in range(m)]

        def cal(row,col):
            nonlocal dp
            x_count = 1 if grid[row][col] == "X" else 0
            y_count = 1 if grid[row][col] == "Y" else 0
            d_count = 1 if grid[row][col] == "." else 0
            if row == 0:
                pre = dp[row][col-1]
                return Calculator(pre.x+x_count,pre.y+y_count,pre.dot+d_count)
            elif col == 0:
                pre = dp[row-1][col]
                return Calculator(pre.x+x_count,pre.y+y_count,pre.dot+d_count)
            else:
                left_pre = dp[row][col-1]
                up_pre = dp[row-1][col]
                left_up_pre = dp[row-1][col-1]
                return Calculator(
                    left_pre.x + up_pre.x - left_up_pre.x + x_count,
                    left_pre.y + up_pre.y - left_up_pre.y + y_count,
                    left_pre.dot + up_pre.dot - left_up_pre.dot + d_count,
                )

        ans = 0

        dp[0][0] = Calculator(
            1 if grid[0][0] == "X" else 0,
            1 if grid[0][0] == "Y" else 0,
            1 if grid[0][0] == "." else 0,
        )


        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                dp[i][j] = cal(i,j)
                if dp[i][j].is_valid():
                    # print(i,j,dp[i][j],dp[i][j])

                    ans += 1
        # print(dp)
        # print(dp[1][1].is_valid())
        return ans


        