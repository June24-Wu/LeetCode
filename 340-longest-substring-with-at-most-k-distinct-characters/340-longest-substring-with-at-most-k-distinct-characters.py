class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0 ; table = {} ; ans = 0
        for right in range(len(s)):
            table[s[right]] = 1 if s[right] not in table else table[s[right]] + 1
            while len(table) > k:
                table[s[left]] -= 1
                if table[s[left]] == 0:
                    del table[s[left]]
                left += 1
            ans = max(ans,right - left + 1)
        return ans