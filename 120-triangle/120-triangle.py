class Solution:
    def minimumTotal(self, nums: List[List[int]]) -> int:
        n = len(nums)
        dp = nums[0].copy()
        for i in range(1,n):
            temp = dp.copy()
            dp = nums[i].copy()
            for j in range(i+1):
                if j == 0:
                    dp[j] += temp[j]
                elif j == i:
                    dp[j] += temp[j-1]
                else:
                    dp[j] += min(temp[j],temp[j-1])
        return min(dp)
        