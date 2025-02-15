class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            good = True
            if i + k < len(nums) and nums[i] <= nums[i+k]:
                good = False
            if i - k >= 0 and nums[i] <= nums[i-k]:
                good = False
            if good:
                ans += nums[i]
        return ans
        