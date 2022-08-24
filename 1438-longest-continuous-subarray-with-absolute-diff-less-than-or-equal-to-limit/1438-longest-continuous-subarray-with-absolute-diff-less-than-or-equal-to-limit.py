class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxheap = [] ; minheap = [] ; table = collections.defaultdict(int)
        ans = 0
        left = 0
        
        def add(num):
            heapq.heappush(maxheap,-num)
            heapq.heappush(minheap,num)
            table[num] += 1
        def isValid():
            while table[-maxheap[0]] == 0:
                heapq.heappop(maxheap)
            while table[minheap[0]] == 0:
                heapq.heappop(minheap)
            return -maxheap[0] - minheap[0] <= limit
        def remove(num):
            table[num] -= 1
        for right in range(len(nums)):
            add(nums[right])
            while not isValid():
                remove(nums[left])
                left += 1
            ans = max(ans,right - left + 1)
        return ans
                
            
        