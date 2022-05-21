class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        visited = set() ; visited.add(beginWord)
        wordList = set(wordList)
        def change(char):
            nonlocal wordList
            char = list(char)
            rt = []
            for index,ch in enumerate(char):
                for i in range(26):
                    newCh = chr(ord("a") + i)
                    char[index] = newCh
                    if "".join(char) in wordList and "".join(char) not in visited:
                        rt.append("".join(char))
                        visited.add("".join(char))
                    char[index] = ch
            return rt
        
        queue = [beginWord]
        step = 0
        while queue != []:
            length = len(queue)
            if endWord in queue:
                return step + 1
            for i in range(length):
                char = queue.pop(0)
                nextWordList = change(char)
                queue.extend(nextWordList)
            step += 1
            # print(queue , " " , step)
        return 0 