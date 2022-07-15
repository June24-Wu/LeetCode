class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        
        def dfs(left,right):
            if (left,right) in memo:
                return memo[(left,right)]
            if left == right:
                memo[(left,right)] = nums[left]
                return nums[left]
            return max(nums[left] - dfs(left+1,right) , nums[right] - dfs(left,right - 1))
        return dfs(0,len(nums) - 1) >= 0
        