class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.pre = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        
    def visit(self, url: str) -> None:
        self.curr.next = Node(url)
        self.curr.next.pre = self.curr
        self.curr = self.curr.next
        return

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.pre != None:
                self.curr = self.curr.pre
        return self.curr.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next != None:
                self.curr = self.curr.next
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)