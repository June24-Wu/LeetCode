import math
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a = set(); n = len(nums)
        for i in range(n-1,-1,-1):
            if nums[i] in a:
                return math.ceil((i+1) / 3)
            a.add(nums[i])
        return 0
        