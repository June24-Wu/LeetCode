class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        for index , first in enumerate(nums):
            newTarget = target - first
            left = index + 1 ; right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < newTarget:
                    cnt += right - left
                    left += 1
                else:
                    right -= 1
        return cnt