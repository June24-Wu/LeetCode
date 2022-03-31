class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones)
        target = target // 2 if target % 2 == 0 else (target // 2 + 1)
        
        dp = [0] * (target + 1)
        
        for item in stones:
            for j in range(target,item-1,-1):
                dp[j] = max(dp[j],dp[j-item] + item)
        
        return abs(sum(stones) - 2*dp[-1])
        