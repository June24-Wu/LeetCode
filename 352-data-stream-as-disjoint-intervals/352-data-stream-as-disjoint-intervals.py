class SummaryRanges:

    def __init__(self):
        self.arr = []
        

    def addNum(self, val: int) -> None:
        bisect.insort(self.arr,val)
        # print(self.arr)

    def getIntervals(self) -> List[List[int]]:
        if len(self.arr) < 1:
            return []
        left = self.arr[0]
        ans = []
        for i in range(1,len(self.arr)):
            if self.arr[i] - self.arr[i-1] > 1:
                ans.append([left,self.arr[i-1]])
                left = self.arr[i]
        ans.append([left,self.arr[-1]])
        return ans


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()