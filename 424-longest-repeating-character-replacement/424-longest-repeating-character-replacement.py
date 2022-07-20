class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        charcnt = [0 for _ in range(26)]
        maxcnt = 0 ; maxLength = 0
        while right < len(s):
            charIndex = ord(s[right]) - ord("A")
            charcnt[charIndex] += 1
            maxcnt = max(maxcnt,charcnt[charIndex])
            while right - left + 1 - maxcnt > k:
                charcnt[ord(s[left]) - ord("A")] -= 1
                left += 1
            maxLength = max(maxLength,right - left + 1)
            right += 1
        return maxLength
            
        