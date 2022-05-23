class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        
        left = 0
        if target > sum(nums):
            return 0
        for right in range(len(nums)):
            while sum(nums[left:right+1]) >= target:
                ans = min(ans,right-left + 1)
                left += 1
        return ans
                
        