class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()
        num = 0 ; sign = 1
        
        def get(val):
            left =  - 2**31 ; right = 2 ** 31 -1
            if val <= left:
                return left
            if val >= right:
                return right
            return val
        for i in range(len(s)):
            if i == 0 and s[i] in ["+","-"]:
                sign = 1 if s[i] == "+" else -1
            elif s[i].isdigit():
                num = num*10 + int(s[i])
            else:
                return get(sign*num)
        
        return get(sign*num)
            
                