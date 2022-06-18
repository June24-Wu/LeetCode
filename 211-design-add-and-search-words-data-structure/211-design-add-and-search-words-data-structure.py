class WordDictionary:

    def __init__(self):
        self.li = [None] * 26
        self.isWord = False
    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            charIndex = ord(char) - ord("a")
            if curr.li[charIndex] == None:
                curr.li[charIndex] = WordDictionary()
            curr = curr.li[charIndex]
        curr.isWord = True
    def search(self, word: str) -> bool:
        return self.__search(self,word)
    def __search(self,dictionary,word):
        curr = dictionary
        for index , char in enumerate(word):
            if char == ".":
                for i in curr.li:
                    if i and self.__search(i,word[index+1:]):
                        return True
                return False
            charIndex = ord(char) - ord("a")
            if curr == None or curr.li[charIndex] == None:
                return False
            curr = curr.li[charIndex]
        return curr.isWord
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)