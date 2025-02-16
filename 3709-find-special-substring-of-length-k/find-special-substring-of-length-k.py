class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        for i in range(n-k+1):
            se = list(set(list(s[i:i+k])))
            if len(se) == 1:
                se = se[0]
                f = True
                if i == 0 or se != s[i-1]:
                    f = True
                else:
                    f = False
                # print(i,se,f)
                if i + k == n or se != s[i+k]:
                    f = True and f
                else:
                    f = False and f
                if f:
                    return True
        return False 
        