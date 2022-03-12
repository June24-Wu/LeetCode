class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        sum_set = sum(set(nums))
        total = (1 + length) * length // 2
        return [sum(nums) - sum_set,total - sum_set]
        