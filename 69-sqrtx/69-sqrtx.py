class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0 ; r = x
        
        while l <= r:
            mid = (l+r) // 2
            print(l , mid , r)
            if mid**2 == x:
                return mid
            if mid**2 > x:
                r = mid - 1
            else:
                l = mid + 1
        return l - 1
        