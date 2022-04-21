class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.val = 0
    def insert(self, key: str, val: int):
        node = self
        for i in key:
            i = ord(i) - ord("a")
            if node.children[i] == None:
                node.children[i] = Trie()
            node = node.children[i]
            node.val += val
    def delete(self, key: str, val: int) -> None:
        node = self
        for i in key:
            i = ord(i) - ord("a")
            if node.children[i] == None:
                node.children[i] = MapSum()
            node = node.children[i]
            node.val -= val
    def sum(self, prefix: str) -> int:
        # find the prefix
        node = self
        for i in prefix:
            i = ord(i) - ord("a")
            node = node.children[i]
            if node == None:
                return 0
        return node.val
class MapSum:
    def __init__(self):
        self.trie = Trie()
        self.map = {}
    def insert(self, key: str, val: int) -> None:
        if key in self.map.keys():
            deletedVal = self.map[key]
            self.trie.delete(key,deletedVal)            
        self.trie.insert(key,val)
        self.map[key] = val
    def sum(self, prefix: str) -> int:
        return self.trie.sum(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)