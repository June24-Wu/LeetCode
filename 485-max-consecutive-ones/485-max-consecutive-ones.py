class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val = 0
        val = 0
        for i in nums:
            if i == 1:
                val += 1
            if i == 0:
                max_val = max(max_val,val)
                val = 0
        return max(max_val,val)
                
        