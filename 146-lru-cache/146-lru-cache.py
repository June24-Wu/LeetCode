class DoubleLinkedList:
    def __init__(self,key:int,val:int):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = DoubleLinkedList(0,0)
        self.tail = DoubleLinkedList(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.cache = {}
        self.capacity = capacity
        self.length = 0

    def get(self, key: int) -> int:
        # find node and move it to the tail
        if key not in self.cache:
            return -1
        node = self.cache[key] # get the node
        self.moveToTail(node)
        # print(self.cache.keys())
        # check = self.head
        # while check != None:
        #     print(check.key,end = " ")
        #     check = check.next
        # print("")
        return node.val
        

    def put(self, key: int, value: int) -> None:
        node = DoubleLinkedList(key,value)
        if key not in self.cache:
            self.cache[key] = node
            self.addLast(node)
            self.length += 1
            if self.length > self.capacity:
                deletedNode = self.deleteHead()
                del self.cache[deletedNode.key]
                self.length -= 1
        else:
            oldNode = self.cache[key]
            self.deleteNode(oldNode)
            self.cache[key] = node
            self.addLast(node)
    
    def moveToTail(self,node):
        self.deleteNode(node)
        self.addLast(node)
    def deleteNode(self,node):
        node.pre.next = node.next
        node.next.pre = node.pre
    def addLast(self,node):
        node.next = self.tail
        node.pre = self.tail.pre
        self.tail.pre.next = node
        self.tail.pre = node
    def deleteHead(self):
        node = self.head.next
        self.deleteNode(node)
        return node
        
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)