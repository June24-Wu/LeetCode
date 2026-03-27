class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.li = []
        self.curr = 0

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.li.append(self.curr)
        
        self.curr += 1

        if self.li:
            return self.curr - self.li[-1] > self.k
        else:
            return self.curr >= self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)