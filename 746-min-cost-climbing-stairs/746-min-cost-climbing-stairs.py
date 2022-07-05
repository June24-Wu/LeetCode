class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return sum(cost)
        for i in range(2,len(cost)):
            minval = min(cost[i - 1],cost[i - 2])
            cost[i] += minval
        return min(cost[-1],cost[-2]) 
        