class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        minVal = float("inf")
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = - nums[i]
                k -= 1
            if abs(nums[i]) < minVal:
                minVal = abs(nums[i])
        
        if k % 2 ==0:
            return sum(nums)
        else:
            return sum(nums) - 2*minVal
        
        
                
        