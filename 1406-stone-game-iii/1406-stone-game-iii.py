class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        preSum = stoneValue.copy()
        for i in range(1,len(preSum)):
            preSum[i] = preSum[i - 1] + preSum[i]
        def get(left,right):
            right = min(len(preSum) - 1,right)
            if left - 1< 0 :
                return preSum[right]
            return preSum[right] - preSum[left - 1]
        
        def dfs(index):
            if index in memo:
                return memo[index]
            res =  - float("inf")
            if index >= len(stoneValue):
                return 0
            for i in range(3):
                res = max(res,get(index,index+i) - dfs(index + i + 1))
            memo[index] = res
            return res
        memo = {}
        ans = dfs(0)
        print(memo)
        print(ans)
        if ans < 0:
            return "Bob"
        if ans > 0:
            return "Alice"
        return "Tie"
        
        