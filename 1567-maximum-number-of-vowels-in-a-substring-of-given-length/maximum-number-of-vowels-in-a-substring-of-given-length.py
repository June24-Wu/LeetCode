class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isValid(char):
            return char in ['a','e','i','o','u']
        curr = 0
        for i in range(k):
            if isValid(s[i]):
                curr += 1
        ans = curr
        for i in range(k,len(s)):
            if isValid(s[i-k]):
                curr -= 1
            if isValid(s[i]):
                curr += 1
            ans = max(ans,curr)
        return ans


        