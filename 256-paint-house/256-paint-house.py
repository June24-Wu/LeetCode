class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        cost = [i for i in costs[0]]
        for house in range(1,len(costs)):
            dp = [float("inf")] * 3
            for color in range(3):
                dp[color] = min(dp[color],costs[house][color] + min(cost[(color + 1) % 3],cost[(color + 2) % 3]))
            cost = dp
        return min(cost)
        