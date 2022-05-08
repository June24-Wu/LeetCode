class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums) / 2
        table = {}
        for i in nums:
            if i not in table:
                table[i] = 0
            table[i] += 1
        for i in table:
            if table[i] >= length:
                return i
        