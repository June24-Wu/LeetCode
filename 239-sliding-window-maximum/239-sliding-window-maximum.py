class Deque:
    def __init__(self):
        self.queue = []
    def pop(self,val):
        if self.queue != [] and self.queue[0] == val:
            self.queue.pop(0)
        return
    def push(self,val):
        while self.queue != [] and val > self.queue[-1] :
            self.queue.pop()
        self.queue.append(val)
        return
    def get_front(self):
        return self.queue[0]
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = Deque()
        return_li = []
        for i in range(k):
            queue.push(nums[i])
        return_li.append(queue.get_front())
        for i in range(k,len(nums)):
            queue.pop(nums[i-k])
            queue.push(nums[i])
            return_li.append(queue.get_front())
        return return_li
            
        
        