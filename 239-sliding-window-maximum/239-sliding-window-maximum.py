
class PQ:
    def __init__(self):
        self.li = []
    def add(self,val):
        while self.li != [] and val > self.li[-1]:
            self.li.pop()
        self.li.append(val)
    def pop(self,val):
        if val == self.li[0]:
            self.li.pop(0)
    def getHead(self):
        return self.li[0]
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = PQ()
        ans = []
        for i in range(k):
            pq.add(nums[i])
        ans.append(pq.getHead())
        for i in range(k,len(nums)):
            pq.pop(nums[i-k])
            pq.add(nums[i])
            ans.append(pq.getHead())
        return ans
            

            
        
        