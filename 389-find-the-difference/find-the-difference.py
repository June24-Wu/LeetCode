class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s) ; t = Counter(t)
        for i in t:
            if t[i] > s[i]:
                return i
        