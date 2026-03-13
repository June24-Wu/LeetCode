class Node:
    def __init__(self,val,key=None):
        self.val = val
        self.pre = None
        self.next = None
        self.key=key

class LRUCache:
    def __init__(self, capacity: int):
        self.m = {}
        self.capacity = capacity
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        node = self.m[key]
        self._delete_node(node)
        self._add_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            node = self.m[key]
            node.val = value
            self._delete_node(node)
            self._add_head(node)
        else:
            node = Node(value,key=key)
            self._add_head(node)
            if self.capacity < 0:
                self._delete_tail()
        
    def _add_head(self,node):
        self.m[node.key] = node
        next = self.head.next
        self.head.next = node
        node.next = next
        next.pre = node
        node.pre = self.head
        self.capacity -= 1
    
    def _delete_node(self,node):
        del self.m[node.key]
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
        self.capacity += 1

    def _delete_tail(self):
        return self._delete_node(self.tail.pre)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)