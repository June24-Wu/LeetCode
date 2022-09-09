class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # minval = min(nums)
        return sum(nums) - min(nums) * len(nums)
        