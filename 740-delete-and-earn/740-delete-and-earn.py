class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        table = {i : nums.count(i) for i in set(nums)}
        nums = sorted(set(nums))
        print(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0] * table[nums[0]]
        
        def get(n):
            if n >= 0:
                return dp[n]
            return 0
        for i in range(1,len(nums)):
            num = nums[i] ; cnt = table[num]
            if nums[i] - nums[i-1] == 1:
                dp[i] = max(num*cnt+get(i-2),dp[i-1])
            else:
                dp[i] = dp[i-1] + num*cnt
        # print(dp)
        
        return dp[-1]