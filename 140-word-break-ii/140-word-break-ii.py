class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        maxLength = max([len(i) for i in wordDict])
        path = []
        def backtracking(word):
            nonlocal path
            nonlocal ans
            if word == "":
                ans.append(" ".join(path))
                return
            for i in range(len(word)+1):
                if i <= maxLength and word[:i] in wordDict:
                    path.append(word[:i])
                    newWord = word[i:]
                    backtracking(newWord)
                    path.pop()
            return
        backtracking(s)
        # print(ans)
        return ans
                
            
        