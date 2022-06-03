class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy
        if len(nums) == 1:
            return 0
        jump = 0 ; right = 0 ; cnt = 0
        
        for i in range(len(nums) - 1):
            jump = max(jump,nums[i] + i)
            if i == right:
                cnt += 1
                right = jump
        return cnt
                
        
        
        
        
        
        
        
        
        
        
        
        
        # DP
        # dp = [float("inf") for _ in range(len(nums))]
        # dp[0] = 0
        # for index , num in enumerate(nums):
        #     for j in range(index+1,index + num + 1):
        #         if j >= len(nums):
        #             return dp[-1]
        #         dp[j] = min(dp[j],dp[index] + 1)
        # return dp[-1]
            