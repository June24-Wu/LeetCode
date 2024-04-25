class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        table = collections.defaultdict(int)
        ans = 1
        for i in range(len(s)):
            charval = ord(s[i])
            table[charval] = max([table[i] + 1 for i in range(charval - k,charval + k + 1)])
            ans = max(table[charval],ans)
        return ans

        