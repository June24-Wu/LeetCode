class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        table = {val : nums.count(val) for val in set(nums)}
        nums = list(set(nums))
        nums.sort()
        dp = [0] * len(nums)
        dp[0] = nums[0] * table[nums[0]]
        for i in range(1,len(nums)):
            curr = nums[i] * table[nums[i]]
            if nums[i] - nums[i - 1] == 1:
                curr = max(curr + dp[i-2],dp[i-1])
            else:
                curr += dp[i - 1]
            dp[i] = curr

        return dp[-1]
        