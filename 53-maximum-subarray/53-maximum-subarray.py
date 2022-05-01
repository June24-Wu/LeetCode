class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i],nums[i]+nums[i-1])
        # print(nums)
        return max(nums)
        