class MedianFinder:

    def __init__(self):
        self.minQueue = list()
        self.maxQueue = list()

    def addNum(self, num: int) -> None:
        if self.minQueue == [] or num <= -self.minQueue[0]:
            heapq.heappush(self.minQueue,-num)
            if len(self.maxQueue) + 1 < len(self.minQueue):
                heapq.heappush(self.maxQueue,-heapq.heappop(self.minQueue))
        else:
            heapq.heappush(self.maxQueue,num)
            if len(self.maxQueue) > len(self.minQueue):
                heapq.heappush(self.minQueue,-heapq.heappop(self.maxQueue))            
    def findMedian(self) -> float:
        if len(self.maxQueue) == len(self.minQueue):
            return (self.maxQueue[0] - self.minQueue[0])/2
        else:
            return - self.minQueue[0]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()