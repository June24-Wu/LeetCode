class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        length = len(columnTitle)
        for idx , i in enumerate(columnTitle):
            ans += (ord(i) - ord("A") + 1) * 26 ** (length - idx - 1)
        return ans
        