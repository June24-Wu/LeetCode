class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        jump = 0
        for i in range(len(nums)):
            jump = max(jump , nums[i] + i)
            if jump <= i:
                break
        return jump >= len(nums) - 1
            
        