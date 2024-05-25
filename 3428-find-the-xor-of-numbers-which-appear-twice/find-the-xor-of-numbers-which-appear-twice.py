class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        nums = Counter(nums)
        a = 0
        for i in nums:
            if nums[i] > 1:
                a = a ^ i
        return a
        