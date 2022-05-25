class Solution:
    def myPow(self, x: float, n: int) -> float:
        def function(val,times):
            if times == 0 :
                return 1
            y = function(val,times // 2)
            if times % 2 == 0:
                return y*y
            return y*y*val
                
        if n == 1:
            return x
        if n == 0:
            return 1
        if n > 0 :
            return function(x,n)
        else:
            return 1 / function(x,-n)
        
        
