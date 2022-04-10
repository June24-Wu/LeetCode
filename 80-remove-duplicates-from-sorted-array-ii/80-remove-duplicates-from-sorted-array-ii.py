class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:return len(nums)
        
        p1 = 2
        p2 = 2
        
        for p2 in range(2,len(nums)):
            if nums[p2] != nums[p1-2]:
                nums[p1] = nums[p2]
                p1 += 1
        return p1