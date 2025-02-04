class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [None for _ in range(n)]
        su = [None for _ in range(n)]
        curr = 1
        for i in range(n):
            curr *= nums[i]
            pre[i] = curr
        curr = 1
        for i in range(n-1,-1,-1):
            curr *= nums[i]
            su[i] = curr
        for i in range(n):
            prev = pre[i-1] if i-1 >= 0 else 1
            suv = su[i+1] if i+1 < n else 1
            nums[i] = prev * suv
        return nums


