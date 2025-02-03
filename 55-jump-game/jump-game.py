class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        jump_left = nums[0]
        if jump_left > 0:
            for i in range(1,len(nums)):
                jump_left -= 1
                jump_left = max(jump_left,nums[i])
                if jump_left <= 0:
                    break
        else:
            i = 0
        return i >= len(nums) - 1
        