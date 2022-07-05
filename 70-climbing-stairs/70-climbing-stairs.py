class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        a = 1 ; b = 1
        for _ in range(1,n):
            c = a + b
            a = b
            b = c
        return b
        
        