class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:return 0

        curr = 0
        jump = 0
        cnt = 0
        for i in range(len(nums)):
            jump = max(jump,i+nums[i])
            if i == curr and curr < len(nums)-1:
                cnt += 1
                curr = jump
            if curr >= len(nums) -1:
                break
        return cnt
        