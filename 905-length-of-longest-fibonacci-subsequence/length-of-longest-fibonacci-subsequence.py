class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[2 for _ in range(n)] for _ in range(n)]
        loc = {}
        ans = 0
        for i in range(n):
            for j in range(i):
                if arr[i] - arr[j] in loc:
                    k = loc[arr[i] - arr[j]]
                    if k < j:
                        dp[i][j] = max(dp[i][j],dp[j][k] + 1)
                        # print(i,j,k,dp[i][j])
                        ans = max(ans,dp[i][j])           
            loc[arr[i]] = i
        return ans
        