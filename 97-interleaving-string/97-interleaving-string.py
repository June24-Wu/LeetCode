class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        p1 = 0 ; p2 = 0 ; m = len(s1) ; n = len(s2) ; length = len(s3)
        s1 += "*" ; s2 += "*"
        if m + n != length:
            return False
        @cache
        def dfs(p1,p2,index):
            if index == length:
                return True
            if s1[p1] == s3[index] and s2[p2] == s3[index]:
                return dfs(p1+1,p2,index+1) or dfs(p1,p2+1,index +1)
            elif s1[p1] == s3[index]:
                return dfs(p1 + 1,p2,index + 1)
            elif s2[p2] == s3[index]:
                return dfs(p1,p2 + 1,index + 1)
            else:
                return False
        return dfs(0,0,0)
            