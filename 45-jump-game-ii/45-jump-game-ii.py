class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0
        for i in range(n):
            step = nums[i]
            for j in range(i+1,i+step + 1):
                if j < n:
                    dp[j] = min(dp[j],dp[i] + 1)
        return dp[-1]