class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        s = [ord(i) - ord("a") for i in s]
        idx = [-1 for _ in range(3)]
        ans = 0
        for i in range(len(s)):
            idx[s[i]] = i
            minv = min(idx)
            if minv > -1:
                ans += minv + 1
        return ans
        