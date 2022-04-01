class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        
        
        
        for j in range(1,target+1):
            for item in nums:
                if j-item < 0:continue
                dp[j] += dp[j-item]
        return dp[-1]
        