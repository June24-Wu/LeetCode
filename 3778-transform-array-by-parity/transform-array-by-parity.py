class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        nums = [i % 2 for i in nums]
        return sorted(nums)
        