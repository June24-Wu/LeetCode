class Node:
    def __init__(self,key,val,pre = None,next = None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.val2node = {}
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def get(self, key: int) -> int:
        # print("get",key,self.val2node)
        if self.val2node.get(key):
            node = self.val2node.get(key)
            key, value = node.key, node.val
            self.__del(node)
            self.__add_head(key,value)
            return self.val2node.get(key).val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.val2node:
            self.__del(self.val2node[key])
        self.__add_head(key,value)
        if len(self.val2node) > self.capacity:
            self.__del_last()
        # print("put",key,value,self.val2node)

    def __add_head(self,key,value):
        node = Node(key,value)
        node_next = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = node_next
        node_next.pre = node
        self.val2node[key] = node
    
    def __del(self,node):
        key = node.key
        del self.val2node[key]
        pre_node = node.pre
        next_node = node.next
        pre_node.next = next_node
        next_node.pre = pre_node
    
    def __del_last(self):
        self.__del(self.tail.pre)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)