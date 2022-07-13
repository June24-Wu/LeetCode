class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        dp = [1 for _ in range(n)]
        dp[0] = 0 ; dp[1] = 0
        mid = int(sqrt(n))
        for i in range(2,mid + 1):
            if dp[i] == 0:
                continue
            for j in range(i**2,n,i):
                dp[j] = 0
        return sum(dp)
                
            
        