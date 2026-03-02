class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        left = 0
        n = len(nums)
        curr = 0; ans = float("inf")
        for right in range(n):
            curr += nums[right]
            while curr >= target:
                ans = min(ans,right - left + 1)
                curr -= nums[left]
                left += 1
            # print(left,right,curr)
        return ans
        