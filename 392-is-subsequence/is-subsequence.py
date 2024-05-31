class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        left = 0
        for right in range(len(t)):
            if t[right] == s[left]:
                left += 1
            if left == len(s):
                break
        return left == len(s)
        