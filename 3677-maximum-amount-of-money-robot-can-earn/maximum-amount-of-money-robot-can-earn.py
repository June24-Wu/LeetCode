class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins); n = len(coins[0])
        dp =[[[0,0,0] for _ in range(n)] for _ in range(m)]
        dp[0][0] = [coins[0][0],max(coins[0][0],0),0] 
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                cell = dp[i][j]

                if coins[i][j] >= 0:
                    if i == 0:
                        pre_cell = dp[i][j-1]
                        dp[i][j] = [
                            pre_cell[0] + coins[i][j],
                            pre_cell[1] + coins[i][j],
                            pre_cell[2] + coins[i][j]
                        ]
                    elif j == 0:
                        pre_cell = dp[i-1][j]
                        dp[i][j] = [
                            pre_cell[0] + coins[i][j],
                            pre_cell[1] + coins[i][j],
                            pre_cell[2] + coins[i][j]
                        ]
                    else:
                        pre_cell = dp[i-1][j]
                        pre_cell2 = dp[i][j-1]
                        dp[i][j] = [
                            max(pre_cell[0],pre_cell2[0]) + coins[i][j],
                            max(pre_cell[1],pre_cell2[1]) + coins[i][j],
                            max(pre_cell[2],pre_cell2[2]) + coins[i][j],
                        ]
                else:
                    if i == 0:
                        pre_cell = dp[i][j-1]
                        dp[i][j] = [
                            pre_cell[0] + coins[i][j],
                            max(pre_cell[1] + coins[i][j], pre_cell[0]),
                            max(pre_cell[2] + coins[i][j], pre_cell[1]),
                        ]
                    elif j == 0:
                        pre_cell = dp[i-1][j]
                        dp[i][j] = [
                            pre_cell[0] + coins[i][j],
                            max(pre_cell[1] + coins[i][j], pre_cell[0]),
                            max(pre_cell[2] + coins[i][j], pre_cell[1]),
                        ]
                    else:
                        pre_cell = dp[i-1][j]
                        pre_cell2 = dp[i][j-1]
                        dp[i][j] = [
                            max(pre_cell[0],pre_cell2[0]) + coins[i][j],
                            max(pre_cell[0],pre_cell2[0],max(pre_cell[1],pre_cell2[1]) + coins[i][j]),
                            max(pre_cell[1],pre_cell2[1],max(pre_cell[2],pre_cell2[2]) + coins[i][j]),
                        ]
        # print(dp)
        return max(dp[-1][-1])

                    
        