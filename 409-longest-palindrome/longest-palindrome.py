class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = Counter(s) ; a = 0 ; v = 0
        for i in s:
            if s[i] % 2 == 0:
                a += s[i]
            else:
                v = 1
                a += s[i] - 1
        return a + v

        