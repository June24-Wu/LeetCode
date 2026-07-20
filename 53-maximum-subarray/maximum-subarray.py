class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr < 0:
                curr = 0
            else:
                ans = max(ans,curr)
        return ans

        