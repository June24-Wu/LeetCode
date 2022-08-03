class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = right = len(nums)
        total = rightval = sum(nums)
        left = leftval = 0
        ans = float("inf") ; index = 0
        for i in range(n):
            leftval += nums[i]
            left += 1;
            rightval  -= nums[i]
            right -= 1
            if right == 0:
                right = 1
            if abs(leftval // left - rightval // right) < ans:
                ans = abs(leftval // left - rightval // right)
                index = i
        return index