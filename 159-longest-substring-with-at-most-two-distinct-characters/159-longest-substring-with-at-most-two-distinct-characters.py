class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        
        left = 0  ; table = collections.defaultdict(int) ; ans = 0
        for right in range(len(s)):
            table[s[right]] += 1
            while len(table) > 2:
                table[s[left]] -= 1
                if table[s[left]] == 0:
                    del table[s[left]]
                left += 1
            ans = max(ans,right - left + 1)
        return ans
        