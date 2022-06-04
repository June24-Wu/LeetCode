class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = [( - nums[0],0)] # (val , index)
        ans = nums[0]
        for i in range(1,len(nums)):
            while i - k > heap[0][1]:
                heapq.heappop(heap)
            val , index = heap[0]
            val = - val
            val += nums[i]
            ans = val
            heapq,heappush(heap,(-val,i))
        return ans
        
   
        # BF DP 做法： TLE
        n = len(nums)
        dp = [ - float("inf") for _ in range(n)]
        dp[0] = nums[0]
        for index , num in enumerate(nums):
            for j in range(1,1 + k):
                if index + j < n:
                    dp[index+j] = max(dp[index+j],dp[index] + nums[index + j])
            # print(index)
            # print(dp)
        return dp[-1]
        