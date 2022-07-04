class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        table = {}
        for i in nums:
            if i not in table:
                table[i] = 0
            table[i] += 1
        for i in range(1,len(nums) + 1):
            if i not in table:
                return i
        return len(nums) + 1