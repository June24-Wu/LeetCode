class Solution:
    
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if abs(target) > sum(nums) or (target + sum(nums)) % 2 == 1: return 0
        left = (target + sum(nums)) // 2
        
        dp = [0 for _ in range(left+1)]
        
        dp[0] = 1
        
        for item in nums:
            for j in range(left,item-1,-1):
                dp[j] += dp[j-item]

        return dp[-1]
                
        
        # ---------------------------backtracking---------------------------
#         self.cnt = 0        
        
#         length = len(nums)
#         def backtracking(start_index,path):
#             if start_index == length:
#                 if path == target:
#                     self.cnt += 1
#                 return
#             backtracking(start_index+1,path + nums[start_index])
#             backtracking(start_index+1,path - nums[start_index])
                
#         backtracking(0,0)
        
#         return self.cnt
# ===============================================dp=============================================
        
        

        