class Median:
    def __init__(self):
        self.min = []
        self.max = []
    def add(self,val:float):
        if self.min == []:
            heapq.heappush(self.min,-val)
            return
        if self.max == []:
            heapq.heappush(self.max,val)
            return
        if val > - self.min[0]:
            heapq.heappush(self.max,val)
        else:
            heapq.heappush(self.min,-val)
        self.restruct()
        return
    def restruct(self):
        while abs(len(self.min) - len(self.max)) >= 1:
            if len(self.min) - len(self.max) == 1:
                break
            if len(self.min) - len(self.max) > 1:
                val = - heapq.heappop(self.min)
                heapq.heappush(self.max,val)
            else:
                val = - heapq.heappop(self.max)
                heapq.heappush(self.min,val)
        return
    def get(self):
        if len(self.min) == len(self.max):
            return (self.max[0] - self.min[0]) / 2
        return  - self.min[0]
    def delete(self,val):
        if val <=  - self.min[0]:
            self.min.pop(self.min.index(-val))
            heapq.heapify(self.min)
        else:
            self.max.pop(self.max.index(val))
            heapq.heapify(self.max)
        self.restruct()
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = Median()
        for i in range(k):
            median.add(nums[i])
        ans = [median.get()]
        for i in range(k,len(nums)):
            # print(median.min)
            # print(median.max)
            median.delete(nums[i-k])
            median.add(nums[i])
            ans.append(median.get())
        return ans
            
        