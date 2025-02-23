class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(i) for i in list(s)]
        while len(s) > 2:
            curr = []
            for i in range(1,len(s)):
                curr.append((s[i] + s[i-1]) % 10)
            s = curr
            # print(s)
        return s[0] == s[1]
        