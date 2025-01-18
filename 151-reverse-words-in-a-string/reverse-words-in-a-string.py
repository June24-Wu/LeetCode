class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        n = len(s); ans = []
        for i in range(n-1,-1,-1):
            ans.append(s[i])
        return " ".join(ans)
        