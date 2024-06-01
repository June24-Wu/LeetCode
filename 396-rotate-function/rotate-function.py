class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        sumv = 0 ; length = len(nums)
        for i in range(len(nums)):
            sumv += i * nums[i]
        sumli = sum(nums) ; ans = sumv
        for i in range(length-1,-1,-1):
            sumv += sumli - length * nums[i]
            ans = max(ans,sumv)
        return ans
        