class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_len = 0
        ans = ""
        length = len(s)
        
        for i in range(len(s)):
            l = i; r = i
            while l >= 0 and r < length and s[l] == s[r]:
                l -= 1
                r += 1
            if r - 1 - (l + 1) + 1 > ans_len:
                ans_len = r - 1 - (l + 1) + 1
                ans = s[l+1:r]
            if i > 0 and s[i] == s[i-1]:
                l = i - 1; r = i
                while l >= 0 and r < length and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - 1 - (l + 1) + 1 > ans_len:
                    ans_len = r - 1 - (l + 1) + 1
                    ans = s[l+1:r]
        return ans
        