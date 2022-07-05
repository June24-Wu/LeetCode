class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for i in nums:
            if i - 1 in nums:
                continue
            curr = i ; length = 1
            while curr + 1 in nums:
                curr += 1
                length += 1
            ans = max(length,ans)
        return ans
        