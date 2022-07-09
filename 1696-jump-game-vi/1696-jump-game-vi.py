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
        
        