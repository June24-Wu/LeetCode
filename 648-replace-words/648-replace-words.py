class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isLast = False
    def add(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isLast = True

    def findPrefix(self,word):
        node = self
        prefix = ""
        for i in word:
            index = ord(i) - ord("a")
            if node.isLast == True:
                break
            prefix += i
            if node.children[index] == None:
                return None
            node = node.children[index]
        return prefix

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        dictionary.sort()
        print(dictionary)
        for i in range(len(dictionary)):
            word = dictionary[i]
            if trie.findPrefix(word) != None:
                dictionary[i] = trie.findPrefix(word)
            else:
                trie.add(word)
        print(trie.findPrefix("cattle"))
        dictionary = list(set(dictionary))
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            if trie.findPrefix(sentence[i]) != None:
                sentence[i] = trie.findPrefix(sentence[i])
        return " ".join(sentence)
            

        