class StockSpanner:

    def __init__(self):
        self.li = []

    def next(self, price: int) -> int:
        ans = 1
        while self.li and price >= self.li[-1][0]:
            _, cnt = self.li.pop()
            ans += cnt
        self.li.append((price,ans))
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)