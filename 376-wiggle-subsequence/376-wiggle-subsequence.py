class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = [0] * len(nums)
        down = [0] * len(nums)      
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    up[i] = max(up[i],down[j] + 1)
                if nums[i] < nums[j]:
                    down[i] = max(down[i],up[j] + 1)
        return max(up[-1],down[-1]) + 1