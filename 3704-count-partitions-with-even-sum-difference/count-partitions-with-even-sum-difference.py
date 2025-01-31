class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = []
        curr = 0
        for idx , i in enumerate(nums):
            curr += i
            prefix.append(curr)
        ans = 0
        for i in range(len(nums) - 1):
            left = prefix[i]
            right = total - left
            if abs(right - left) % 2 == 0:
                ans += 1
        return ans

        