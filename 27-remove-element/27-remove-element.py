class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # if len(nums) == 1 and nums[0] == val:
        #     return 0
        # if len(nums) == 1 and nums[0] != val:
        #     return 1
        p1 = 0
        p2 = 0
        
        while p2 < len(nums):
            nums[p1] = nums[p2]
            if nums[p2] == val:
                p2 +=1
            else:
                p1+=1
                p2+=1
            
        return p1
            
                
        