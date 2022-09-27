class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7 
        @cache
        def dfs(index,curr_sum):
            if index == n:
                return curr_sum == target
            res = 0
            for i in range(1,min(k,target - curr_sum) + 1):
                res = (res +  dfs(index+1,curr_sum+i)) % mod
            return res
        return dfs(0,0) % mod