class Solution:
    def __rob(self, nums: List[int]) -> int:
        if nums == None or nums == []: return 0
        length = len(nums)
        if length == 1:return nums[0]
        dp = [0for _ in range(length)]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,length):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
    def rob(self, nums: List[int]) -> int:
        if nums == [] or not nums: return 0
        length = len(nums)
        if length == 1:return nums[0]
        return max(self.__rob(nums[0:length-1]),self.__rob(nums[1:length]))
    
        