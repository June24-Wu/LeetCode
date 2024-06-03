class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left = 0
        for right in range(len(s)):
            if s[right] == t[left]:
                left += 1
            if left == len(t):
                break
        return len(t) - left

        