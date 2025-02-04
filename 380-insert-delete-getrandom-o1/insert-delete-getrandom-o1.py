class RandomizedSet:

    def __init__(self):
        self.li = []
        self.table = {}
        

    def insert(self, val: int) -> bool:
        if val in self.table.keys(): return False
        self.table[val] = len(self.li)
        self.li.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.table.keys():return False
        index = self.table[val]
        final_val = self.li[-1]
        self.li[index] = final_val
        self.table[final_val] = index
        del self.table[val]
        self.li.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.li)