class Node:
    def __init__(self,val):
        self.val = val
        self.pre = None
        self.next = None
class MaxStack:

    def __init__(self):
        self.pq = []
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.table = collections.defaultdict(list)

    def push(self, x: int) -> None:
        pre = self.tail.pre
        node = Node(x)
        pre.next = node
        node.next = self.tail
        node.pre = pre
        self.tail.pre = node
        heapq.heappush(self.pq,-x)
        self.table[x].append(node)
    def pop(self) -> int:
        node = self.tail.pre
        self.delete(node)
        self.table[node.val].pop()
        return node.val
    def top(self) -> int:
        return self.tail.pre.val
    def peekMax(self) -> int:
        while self.table[-self.pq[0]] == []:
            heapq.heappop(self.pq)
        return - self.pq[0]

    def popMax(self) -> int:
        while self.table[-self.pq[0]] == []:
            heapq.heappop(self.pq)
        val = - heapq.heappop(self.pq)
        node = self.table[val].pop()
        self.delete(node)
        return val
    def delete(self,node):
        next = node.next
        pre = node.pre
        pre.next = next
        next.pre = pre
        return


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()