class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        length = len(nums)
        nums.insert(0,1)
        nums.append(1)
        
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for i in range(length,-1,-1):
            for j in range(i+1,len(nums)):
                for k in range(i+1,j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + nums[i]*nums[j]*nums[k]
                    )
        return dp[0][len(nums)-1]