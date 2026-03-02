class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = collections.defaultdict(int)
        def is_valid(m):
            for i in m.values():
                if i > 1:
                    return False
            return True
        left = 0; ans = 0
        for right in range(len(s)):
            m[s[right]] += 1
            while not is_valid(m):
                m[s[left]] -= 1
                left += 1
            ans = max(ans,right-left+1)
        return ans
        