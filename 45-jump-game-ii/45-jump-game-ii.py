class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf") for _ in range(len(nums))]
        dp[0] = 0
        for index , num in enumerate(nums):
            for j in range(index+1,index + num + 1):
                if j < len(nums):
                    dp[j] = min(dp[j],dp[index] + 1)
            # print(dp)
        return dp[-1]
            