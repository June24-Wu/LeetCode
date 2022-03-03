class MinStack:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.stack2 == []:
            self.stack2.append(val)
        else:
            value = self.stack2.pop()
            if val <= value:
                self.stack2.append(value)
                self.stack2.append(val)
            else:
                self.stack2.append(value)
            
    def pop(self) -> None:
        a = self.stack.pop()
        
        b = self.stack2.pop()
        if a != b:
            self.stack2.append(b)
        
    def top(self) -> int:
        value = self.stack.pop()
        self.stack.append(value)
        return value
        

    def getMin(self) -> int:
        a = self.stack2.pop()
        self.stack2.append(a)
        return a


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()