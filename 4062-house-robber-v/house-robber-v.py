class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1]) if colors[0] == colors[1] else sum(nums[:2])
        for i in range(2,n):
            if colors[i] == colors[i-1]:
                dp[i] = max(nums[i] + dp[i-2],dp[i-1])
            else:
                dp[i] = nums[i] + dp[i-1]
        # print(dp)
        return dp[-1]


        