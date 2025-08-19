class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        curr_len = 0
        for idx , item in enumerate(nums):
            if item == 0:
                curr_len += 1
            else:
                ans += (1 + curr_len) * curr_len // 2
                curr_len = 0
        return ans + (1 + curr_len) * curr_len // 2

        