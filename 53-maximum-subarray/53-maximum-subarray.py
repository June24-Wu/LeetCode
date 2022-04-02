class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1,len(nums)):
            if nums[i] + nums[i-1] >= 0:
                nums[i] = max(nums[i],nums[i]+nums[i-1])
        return max(nums)
        
#         for i in range(len(nums)-2,-1,-1):
#             if nums[i+1] >= 0:
#                 nums[i] = nums[i] + nums[i+1]
        
#         return max(nums)
        