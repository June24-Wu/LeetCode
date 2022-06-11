class TwoSum:
    
    def __init__(self):
        self.table = {}
    def add(self, number: int) -> None:
        if number not in self.table:
            self.table[number] = 0
        self.table[number] += 1
    def find(self, value: int) -> bool:
        for i in self.table:
            if value - i == i:
                if self.table[i] >= 2:
                    return True     
            elif (value - i) in self.table:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)