class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def dfs(n):
            if int(n) != n or n <= 0:
                return False
            if n == 1:
                return True 
            return dfs(n/3)
        return dfs(n)
            
        