class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = {}
        for i in range(len(s)):
            if s[i] not in table:
                table[s[i]] = t[i]
            else:
                if table[s[i]] != t[i]:
                    return False
        table = {}
        for i in range(len(s)):
            if t[i] not in table:
                table[t[i]] = s[i]
            else:
                if table[t[i]] != s[i]:
                    return False
                        
        return True
        