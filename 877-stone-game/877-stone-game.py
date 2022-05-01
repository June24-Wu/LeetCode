class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        # dp 
        length = len(nums)
        dp = [0 for _ in range(length)]
        for i in range(length-1,-1,-1):
            temp = dp.copy()
            dp[i] = nums[i]
            for j in range(i+1,length):
                dp[j] = max(nums[j]-dp[j-1],nums[i] - temp[j])
            # print(dp)
        return dp[-1] > 0 
        