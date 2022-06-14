class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        mod = 10 ** 9 + 7
        
        memo = {}
        def dfs(idx, step):
            if idx == 0 and step == 0:
                return 1
            if step == 0:
                return 0
            if (idx,step) in memo:
                return memo[(idx,step)]
			# option 1: stay
            ans = dfs(idx, step - 1)
            if idx + 1 < arrLen:
				# option 2: to the right direction
                ans += dfs(idx + 1, step - 1)
            
            if idx - 1 >= 0:
				# option 3: to the left direction
                ans += dfs(idx - 1, step - 1)
            memo[(idx,step)] = ans % mod
            return ans % mod
        
        return dfs(0, steps)