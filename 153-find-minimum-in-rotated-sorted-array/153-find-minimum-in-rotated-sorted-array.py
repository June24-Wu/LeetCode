class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 ; right = len(nums) - 1
        if nums[0] <= nums[-1]:
            return nums[0]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        