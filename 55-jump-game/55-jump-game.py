class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        index = 0
        i  = nums[0]
        while i > 0 and index < len(nums)-1:
            index += 1
            i-=1
            if i >= nums[index]:
                continue
            else:
                i = nums[index]
        return index >= len(nums) -1
            
            
            
            
        