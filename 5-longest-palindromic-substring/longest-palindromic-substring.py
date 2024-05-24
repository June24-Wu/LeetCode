class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for idx , item in enumerate(s):
            # 1
            left = idx ; right = idx + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1 ; right += 1
            left += 1 ; right -= 1
            if right - left + 1 > len(ans):
                ans = s[left:right+1]
            
            # 2
            left = idx ; right = idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1 ; right += 1
            left += 1 ; right -= 1
            if right - left + 1 > len(ans):
                ans = s[left:right+1]
        return ans
        