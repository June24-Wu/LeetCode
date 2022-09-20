class MyCircularQueue:

    def __init__(self, k: int):
        self.li = [None for _ in range(k)]
        self.k = k
        self.left = 0
        self.right = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.li[self.right % self.k] = value
        self.right += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.li[self.left % self.k]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.li[(self.right - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.left == self.right

    def isFull(self) -> bool:
        return self.right - self.left == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()