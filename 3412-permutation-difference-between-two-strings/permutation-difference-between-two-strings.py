class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        for idx , i in enumerate(s):
            ans += abs(idx - t.index(i))
        return ans
        