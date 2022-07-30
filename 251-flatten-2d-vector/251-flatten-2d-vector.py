class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.li = []
        for li in vec:
            for num in li:
                self.li.append(num)
        self.length = len(self.li)
        self.curr = -1

    def next(self) -> int:
        self.curr += 1
        return self.li[self.curr]
        

    def hasNext(self) -> bool:
        return self.curr < self.length - 1
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()