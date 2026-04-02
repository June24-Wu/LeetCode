class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        m = collections.defaultdict(int)

        maxv = float("-inf")
        for i in range(len(cost)):
            m[s[i]] += cost[i]
            maxv = max(maxv,m[s[i]])
        return sum(cost) - maxv
        