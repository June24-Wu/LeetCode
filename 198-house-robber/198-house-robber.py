class Solution:
    def rob(self, nums: List[int]) -> int:
        # if nums == None or nums == []:
        #     return 0 
        # length = len(nums)
        # if length == 1:
        #     return nums[0]
        # dp = [0 for _ in range(length)]
        # dp[0] = nums[0]
        # dp[1] = max(nums[0],nums[1])
        # for i in range(2,length):
        #     dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        # return dp[-1]
        
        
        if len(nums) <= 2: return max(nums)
        nums[1] = max(nums[0:2])
        for i in range(2,len(nums)):
            nums[i] = max(nums[i] + nums[i-2],nums[i-1])
        return nums[-1]
        