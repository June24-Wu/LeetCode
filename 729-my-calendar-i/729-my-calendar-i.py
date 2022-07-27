class MyCalendar:

    def __init__(self):
        self.table = []

    def book(self, start: int, end: int) -> bool:
        for idx , (left,right) in enumerate(self.table):
            if right <= start:
                continue
            if left >= end:
                self.table.insert(idx,(start,end))
                return True
            else:
                return False
        self.table.append((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)