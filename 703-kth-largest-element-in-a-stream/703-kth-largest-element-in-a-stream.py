class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.length = k
        nums.sort()
        if len(nums) >= k:
            self.heap = nums[len(nums)-k:]
        else:
            self.heap = nums[:]
    def add(self, val: int) -> int:
        if len(self.heap) < self.length:
            heapq.heappush(self.heap,val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        # print(self.heap)
        return self.heap[0]
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)