class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans = 0
        for idx, i in enumerate(nums):
            start = max(0,idx - i)
            for j in range(start,idx+1):
                ans += nums[j]
        return ans
        