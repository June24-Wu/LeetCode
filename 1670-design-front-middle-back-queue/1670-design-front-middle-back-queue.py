class FrontMiddleBackQueue(object):

    def __init__(self):
        self.A = [] # taking an empty queue

    def pushFront(self, val):
        self.A.insert(0, val) #as using append we push the elem at the end also appendleft is there in deque. So in order to push elem in the front we have to use insert as we could push elem at the desired location which is front. 

    def pushMiddle(self, val):
        self.A.insert(len(self.A) // 2, val)

    def pushBack(self, val):
        self.A.append(val) # insert is used to push the element in the desired location. But in here we have to push at end which append() do.

    def popFront(self):
        return (self.A or [-1]).pop(0) # (self.A or [-1]) = if we have any value in self.A then we will get that using pop(0(index is for front)) or we will get -1.

    def popMiddle(self):
        return (self.A or [-1]).pop((len(self.A) - 1) // 2) # (self.A or [-1]) = if we have any value in self.A then we will get that using pop((len(self.A) - 1) / 2(middle index )) or we will get -1.

    def popBack(self):
        return (self.A or [-1]).pop()  # (self.A or [-1]) = if we have any value in self.A then we will get that using pop()(last index) or we will get