class Trie:
    def __init__(self):
        self.children = {}
        self.word = None
    def add(self,word):
        curr = self
        for i in word:
            if i not in curr.children:
                curr.children[i] = Trie()
            curr = curr.children[i]
        curr.word = word
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for word in products:
            trie.add(word)
        ans = []
        temp = []
        def dfs(node):
            nonlocal temp
            if node.word != None:
                temp.append(node.word)
            for i in node.children:
                dfs(node.children[i])
        curr = trie
        for i in searchWord:
            if i not in curr.children:
                break
            curr = curr.children[i]
            temp = []
            dfs(curr)
            temp.sort()
            ans.append(temp[:3])
        while len(ans) < len(searchWord):
            ans.append([])
        return ans