class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        pre = 0 ; curr = 1
        for _ in range(1,n):
            temp = curr + pre
            pre = curr
            curr = temp
        return curr
            
            
        