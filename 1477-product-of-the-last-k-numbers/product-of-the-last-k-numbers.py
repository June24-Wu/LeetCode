class ProductOfNumbers:

    def __init__(self):
        self.count0 = [0]
        self.product = [1]
        
    def add(self, num: int) -> None:
        if num == 0:
            self.count0.append(self.count0[-1] + 1)
            self.product.append(self.product[-1])
        else:
            self.product.append(self.product[-1] * num)
            self.count0.append(self.count0[-1])
        

    def getProduct(self, k: int) -> int:
        if self.count0[-1] != self.count0[-1-k]:
            return 0
        else:
            return self.product[-1] // self.product[-1-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)