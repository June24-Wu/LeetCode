class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = [0] * len(nums)
        down = [0] * len(nums)
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        return max(down[-1],up[-1]) + 1
         
        
        
        
        
        
        
        
        # O(n2)
        # up = [0] * len(nums)
        # down = [0] * len(nums)      
        # for i in range(len(nums)):
        #     for j in range(i-1,-1,-1):
        #         if nums[i] > nums[j]:
        #             up[i] = max(up[i],down[j] + 1)
        #         if nums[i] < nums[j]:
        #             down[i] = max(down[i],up[j] + 1)
        # return max(up[-1],down[-1]) + 1