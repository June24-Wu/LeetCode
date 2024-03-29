class StockPrice:

    def __init__(self):
        self.table = collections.defaultdict(int)  # time stamp : price
        self.maxheap = [] # ( - price , timestamp)
        self.minheap = [] # (price , timestamp)
        self.curr_list = [] #  （- timestamp ， price)
        

    def update(self, timestamp: int, price: int) -> None:
        self.table[timestamp] = price
        heapq.heappush(self.curr_list,(- timestamp , price))
        heapq.heappush(self.minheap,(price , timestamp))
        heapq.heappush(self.maxheap,( - price , timestamp))
        
        

    def current(self) -> int:
        while self.table[-self.curr_list[0][0]] != self.curr_list[0][1]:
            heapq.heappop(self.curr_list)
        return self.curr_list[0][1]

    def maximum(self) -> int:
        while self.table[self.maxheap[0][1]] != - self.maxheap[0][0]:
            heapq.heappop(self.maxheap)
        return  - self.maxheap[0][0]

    def minimum(self) -> int:
        while self.table[self.minheap[0][1]] != self.minheap[0][0]:
            heapq.heappop(self.minheap)
        return self.minheap[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()