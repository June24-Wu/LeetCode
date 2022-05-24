class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixSum = [0]
        for i in nums:
            prefixSum.append(prefixSum[-1] + i)
        
        queue = []
        ans = float("inf")
        for index,item in enumerate(prefixSum):
            while queue != [] and item < prefixSum[queue[-1]]:
                queue.pop()
            while queue != [] and item - prefixSum[queue[0]] >= k:
                ans = min(ans,index - queue.pop(0))
            queue.append(index)
        ans = -1 if ans == float("inf") else ans
        return ans
        