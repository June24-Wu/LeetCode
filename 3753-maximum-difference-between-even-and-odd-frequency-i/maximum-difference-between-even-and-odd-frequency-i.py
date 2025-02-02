class Solution:
    def maxDifference(self, s: str) -> int:
        s = Counter(s)
        s = [v for k,v in s.items()]
        s.sort()
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i] % 2 == 1:
                right = s[i]
                break
        for i in range(n):
            if s[i] % 2 == 0:
                return right - s[i]
        # return 1
        