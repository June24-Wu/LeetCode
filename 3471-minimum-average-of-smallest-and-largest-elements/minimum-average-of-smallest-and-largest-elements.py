class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left = 0 ; right = len(nums)-1
        avg = float("inf")
        while left < right:
            avg = min(avg,(nums[left] + nums[right])/2)
            left += 1
            right -= 1
        return avg
        