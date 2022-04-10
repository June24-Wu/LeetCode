class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 官方解法
        p1 = 1
        
        for i in range(1,len(nums)):
            if nums[p1-1] != nums[i]:
                nums[p1] = nums[i]
                p1 += 1
        return p1
        
        
        
        
        
        # 解法 1
#         p1 = 0 ; p2 = 1
        
#         while p2 < len(nums):
#             if nums[p1] == nums[p2]:
#                 p2 += 1
#             else:
#                 nums[p1+1] = nums[p2]
#                 p1 += 1
#         return p1 +1
        