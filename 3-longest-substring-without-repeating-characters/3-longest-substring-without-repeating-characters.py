class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 ; right = 0
        table = set()
        length = 0
        while right < len(s):
            if s[right] not in table:
                table.add(s[right])
                right += 1
                length = max(length,right-left)
            else:
                table.remove(s[left])
                left += 1
        return length