class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:return 1
        
        p1 = 0
        p2 = 1
        
        length = 0
        while p2 < len(nums):
            if nums[p2] > nums[p2-1]:
                p2 += 1
            else:
                length = max(length,p2-p1)
                p1=p2
                p2 += 1
                
                
        return max(length,p2-p1)
                
        