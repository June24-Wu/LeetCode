class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ans = []
        plist = [0] * 26
        for i in p:
            plist[ord(i) - ord("a")] += 1
        slist = [0] * 26
        for i in range(len(p)):
            slist[ord(s[i]) - ord("a")] += 1
        if slist == plist:
            ans.append(0)
        for i in range(len(p),len(s)):
            slist[ord(s[i-len(p)]) - ord("a")] -= 1
            slist[ord(s[i]) - ord("a")] += 1
            if slist == plist:
                ans.append(i-len(p) + 1)
        return ans
            
            