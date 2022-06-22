class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        new_words = []
        for i in words:
            new_words.append((len(i),i))
        new_words.sort()
        words = []
        for n, word in new_words:
            words.append(word)
        def isValid(first , second):
            if len(second) - len(first) != 1:
                return False
            p1 = 0  ; p2 = 0
            diff = 0
            while p1 < len(first) and p2 < len(second):
                if first[p1] == second[p2]:
                    p1 += 1; p2 += 1
                else:
                    p2 += 1
                    diff += 1
            return p1 == len(first)
        dp = [1 for _ in range(len(words))]
        # print(words)
        for i in range(len(words)):
            for j in range(i-1,-1,-1):
                if len(words[i]) - len(words[j]) > 1:
                    break
                if len(words[i]) - len(words[j]) == 1 and isValid(words[j],words[i]):
                    dp[i] = max(dp[i],dp[j] + 1)
        # print(dp)
        return max(dp)
        