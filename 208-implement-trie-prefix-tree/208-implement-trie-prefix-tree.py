class Trie:

    def __init__(self):
        self.isLast = False
        self.children = [None for _ in range(26)]
        
    def searchPrefix(self,word:str):
        node = self
        for i in word:
            i = ord(i) - ord("a")
            if node.children[i] == None:
                return None
            node = node.children[i]
        return node
    def insert(self, word: str) -> None:
        node = self
        for i in word:
            i = ord(i) - ord("a")
            if not node.children[i]:
                node.children[i] = Trie()
            node = node.children[i]
        node.isLast = True
    def search(self, word: str) -> bool:
        if self.searchPrefix(word) == None:return False
        return self.searchPrefix(word).isLast
    
    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)