class Solution(object):
    def minOperations(self, nums, x):
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        left = 0;
        curr = 0
        ans = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr > target:
                curr -= nums[left]
                left += 1
            if curr == target:
                ans = max(ans,right-left+1)
        if ans == 0:
            return - 1
        return len(nums) - ans
        