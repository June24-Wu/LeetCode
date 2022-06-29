class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur , ans = 0 , 0
        for i in nums:
            cur = max(0,cur + i)
            ans = max(cur , ans)
        if ans == 0:
            return max(nums)
        return ans
        