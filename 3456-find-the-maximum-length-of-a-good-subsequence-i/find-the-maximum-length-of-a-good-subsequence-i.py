class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[1 for _ in range(k+2)] for _ in range(len(nums))]
        ans = 1
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i] != nums[j]:
                    for t in range(k):
                        dp[i][t+1] = max(dp[i][t+1],dp[j][t] + 1)
                        ans = max(ans,dp[i][t+1])
                else:
                    for t in range(k+1):
                        dp[i][t] = max(dp[i][t],dp[j][t] + 1)
                        ans = max(ans,dp[i][t])
        return ans


        