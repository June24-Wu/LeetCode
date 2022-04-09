class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left , right = 0 , len(arr) - 1
        
        def get(n):
            if n < 0 or n >= len(arr):
                return  - float("inf")
            return arr[n]
        
        while left <= right:
            mid = (left + right) // 2
            if get(mid) > get(mid - 1) and get(mid) > get(mid+1):
                return mid
            elif get(mid) < get(mid+1):
                left = mid + 1
            else:
                right = mid - 1
        return mid
        