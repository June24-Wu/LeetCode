class Solution:
    def superEggDrop(self, num: int, floor: int) -> int:


        dp = [[float("inf") for _ in range(floor+1)] for _ in range(num+1)]
        def recursion(k,n):
            if k == 0: return 0
            if k == 1:return n 
            if n <= 1:return n
            if dp[k][n] != float("inf"):
                return dp[k][n]
            l = 1 ; r = n+1
            while l < r:
                mid = (l+r) // 2
                if recursion(k-1,mid-1) >= recursion(k,n-mid):
                    r = mid
                else:
                    l = mid + 1
            dp[k][n] = 1 + max(recursion(k-1,l-1), recursion(k,n-l))
            return dp[k][n]
        return recursion(num,floor)
            
        