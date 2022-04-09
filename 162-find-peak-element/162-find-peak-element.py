class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:return 0
        def get(n):
            if n == -1 or n == len(nums):
                return  - float("inf")
            return nums[n]
        
        left , right = 0,len(nums) - 1
        
        while left <= right:
            mid = (left + right)//2
            if get(mid) > get(mid+1) and get(mid) > get(mid-1):
                return mid
            elif get(mid) < get(mid+1):
                left = mid + 1
            else:
                right = mid - 1 
        return mid
                
        