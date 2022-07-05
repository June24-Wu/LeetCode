class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane
        ans = - float("inf") ; curr = 0
        for i in nums:
            curr = max(0,curr + i)
            ans = max(ans,curr)
        if ans == 0:
            return max(nums)
        return ans
        