class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            idx = ord(char) - ord("a")
            curr.children[idx] = curr.children.get(idx,Trie())
            curr = curr.children[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self
        for char in word:
            idx = ord(char) - ord("a")
            if not curr.children.get(idx,None):
                return False
            curr = curr.children.get(idx)
        return curr.is_end 

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            idx = ord(char) - ord("a")
            if not curr.children.get(idx,None):
                return False
            curr = curr.children.get(idx)
        return True 

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)