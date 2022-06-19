class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.table = {}
        for index,i in enumerate(wordsDict):
            if i not in self.table:
                self.table[i] = []
            self.table[i].append(index)
    def shortest(self, word1: str, word2: str) -> int:
        ans = float("inf")
        for first in self.table[word1]:
            for second in self.table[word2]:
                ans = min(ans,abs(first - second))
        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)