class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]
        curr = 1
        for i in range(n):
            prefix[i] = curr
            curr *= nums[i]
        curr = 1
        for i in range(n-1,-1,-1):
            suffix[i] = curr
            curr *= nums[i]
        ans = [0 for _ in range(n)]
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]
        return ans
        