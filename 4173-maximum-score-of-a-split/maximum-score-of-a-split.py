class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        suffixmin = [None for _ in range(n)]
        prefix_sum = [None for _ in range(n)]

        minval = float("inf")
        for i in range(n-1,-1,-1):
            suffixmin[i] = minval
            minval = min(nums[i],minval)
        
        prefix = 0
        ans = float("-inf")
        for i in range(n):
            prefix += nums[i]
            prefix_sum[i] = prefix
            ans = max(prefix_sum[i] - suffixmin[i],ans)
        # print(prefix_sum)
        # print(suffixmin)
        return ans


        