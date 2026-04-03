class Solution:
    def maxDistinct(self, s: str) -> int:
        ans = 0
        m = set()

        for i in s:
            if i not in m:
                ans += 1
                m.add(i)
        return ans
        