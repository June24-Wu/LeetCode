class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}
        
        def dfs(index,m):
            nonlocal memo
            if (index,m) in memo:
                return memo[(index,m)]
            if 2*m >= n - index:
                memo[(index,m)] = sum(piles[index:])
                return sum(piles[index:])
            res =  - float("inf")
            for i in range(1,2*m + 1):
                res = max(res,sum(piles[index:index+i]) - dfs(index+i,max(m,i)))
            memo[(index,m)] = res
            return res
        ans = (dfs(0,1) + sum(piles)) // 2
        # print(memo)
        return ans