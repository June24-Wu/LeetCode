class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        minVal = float("inf")
        total = 0
        index = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                minVal = min(minVal,i-index + 1)
                total -= nums[index]
                index += 1
                
        return minVal
        