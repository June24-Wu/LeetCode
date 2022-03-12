class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        table = {}
        for i in nums:
            if i in table.keys():
                return i
            else:
                table[i] = 1
        