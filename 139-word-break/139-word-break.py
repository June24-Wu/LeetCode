class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(index):
            if index == len(s):
                return True
            flag = False
            for word in wordDict:
                length = len(word)
                if s[index:index + length] == word:
                    flag = dfs(index + length)
                if flag:
                    return flag
            return False
        return dfs(0)