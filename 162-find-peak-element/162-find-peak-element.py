class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        flag = None
        if len(nums) == 1:
            return 0
        def get(index):
            if 0 <= index < len(nums):
                return nums[index]
            return - float("inf")
        
        def dfs(left,right):
            nonlocal flag
            if flag != None:
                return
            if left > right or left < 0 or right >= len(nums):
                return
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                flag = mid
                return
            dfs(left,mid - 1)
            dfs(mid + 1,right)
            return
        dfs(0,len(nums) - 1)
        return flag
        