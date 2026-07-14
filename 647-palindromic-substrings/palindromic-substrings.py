class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        length = len(s)
        for i in range(length):
            l = i  ; r = i
            while l >= 0 and r < length and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            if i > 0 and s[i] == s[i-1]:
                l = i - 1  ; r = i
                while l >= 0 and r < length and s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
        return ans


        