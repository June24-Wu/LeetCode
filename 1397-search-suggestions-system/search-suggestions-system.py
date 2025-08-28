from sortedcontainers import SortedList

class Trie:
    def __init__(self):
        self.children = {}
        self.list = SortedList()
    def add(self,word):
        curr = self
        for char in word:
            curr.children[char] = curr.children.get(char,Trie())
            curr = curr.children[char]
            curr.list.add(word)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        trie = Trie()
        for i in products:
            trie.add(i)

        curr = trie
        for word in searchWord:
            curr = curr.children.get(word,Trie())
            ans.append(curr.list[:3])
        return ans
        
        