class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        left = 0 ; ans = 0
        for i in range(3 * 10**5):
            if left == len(nums):
                break
            if i < nums[left]:
                continue
            ans += i - nums[left]
            left += 1
        return ans
        