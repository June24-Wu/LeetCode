class FreqStack:

    def __init__(self):
        self.table = collections.defaultdict(list) # {val : [idx,indx]}
        self.cnt = collections.defaultdict(list)  # { cnt : [val,val]}
        self.maxCnt = 0
        self.curr = 0
    def push(self, val: int) -> None:
        originCnt = len(self.table[val])
        self.table[val].append(self.curr)
        self.cnt[originCnt+1].append(val)
        self.maxCnt = max(self.maxCnt,originCnt + 1)
        self.curr += 1

    def pop(self) -> int:
        pop_val = self.cnt[self.maxCnt].pop()
        self.table[pop_val].pop()
        if self.cnt[self.maxCnt] == []:
            self.maxCnt -= 1
        return pop_val