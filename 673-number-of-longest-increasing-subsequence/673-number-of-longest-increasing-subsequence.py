class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        table = collections.defaultdict(int)
        n = len(nums)
        # table[1] = n
        dp = [(1,1) for _ in range(n)]
        
        for i in range(n):
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    length , cnt = dp[j]
                    if length + 1 > dp[i][0]:
                        dp[i] = (length + 1,cnt)
                    elif length + 1 == dp[i][0]:
                        dp[i] = (length+1,dp[i][1] + cnt)
            # print(dp)
        dp.sort(key = lambda x : (-x[0],x[1]))
        maxlength = dp[0][0] ; ans = 0
        for length , cnt in dp:
            if length == maxlength:
                ans += cnt
            else:
                break
        return ans
                
        