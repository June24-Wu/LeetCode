class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[0] = nums.copy()
        for i in range(1,n):
            for j in range(n-i):
                dp[i][j] = (dp[i-1][j] + dp[i-1][j+1]) % 10
        return dp[-1][0]