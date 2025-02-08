class NumberContainers:

    def __init__(self):
        self.m = collections.defaultdict(list)
        self.li = collections.defaultdict(int)

    def change(self, index: int, number: int) -> None:
        self.li[index] = number
        heapq.heappush(self.m[number],index) 

    def find(self, number: int) -> int:
        while self.m[number]:
            if self.li[self.m[number][0]] != number:
                heapq.heappop(self.m[number])
            else:
                break
        if self.m[number]:
            return self.m[number][0]
        else:
            return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)