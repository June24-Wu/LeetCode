class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [None for _ in range(n)]
        right = [None for _ in range(n)]

        left[0] = 1
        for i in range(1,n):
            left[i] = nums[i-1] * left[i-1]
        right[-1] = 1
        for i in range(n-2,-1,-1):
            right[i] = nums[i+1] * right[i+1]
        # print(left)
        # print(right)
        return [left[i] * right[i] for i in range(n)]
        