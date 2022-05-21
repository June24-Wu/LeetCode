class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        bfs = collections.deque()
        bfs.append((beginWord, 1))
        while bfs:
            word, length = bfs.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordset and newWord != word:
                        wordset.remove(newWord)
                        bfs.append((newWord, length + 1))
        return 0