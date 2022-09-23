class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        
        @cache
        def dfs(n):
            if n == 0 or n == 1:
                return 1
            sumval = 0
            for i in range(0,n,2):
                sumval += dfs(i) * dfs(n-2-i)
            return sumval
        return dfs(numPeople) % (10 ** 9  + 7)
        