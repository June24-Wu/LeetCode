class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curr = 0
        ans = 0
        table  = {0:-1}
        for idx , i in enumerate(nums):
            if i == 0:
                curr -= 1
            else:
                curr += 1
            if curr in table:
                ans = max(ans, idx - table[curr])
            else:
                table[curr] = idx
        return ans
        