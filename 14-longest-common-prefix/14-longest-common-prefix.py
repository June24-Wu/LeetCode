class PrefixTree:
    def __init__(self,val):
        self.children = {}
        self.val = val
    def add(self,word):
        word = " " if word == "" else word
        curr = self
        for i in word:
            if i not in curr.children:
                curr.children[i] = PrefixTree(i)
            curr = curr.children[i]
        return
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tree = PrefixTree("")
        length = float("inf")
        for i in strs:
            tree.add(i)
            length = min(len(i),length)
        curr = tree
        ans = ""
        while len(curr.children) == 1 and len(ans) <= length:
            key = list(curr.children.keys())[0]
            curr = curr.children[key]
            ans += curr.val
        return ans[:length]
        