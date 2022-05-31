class Solution:
    def calculate(self, s: str) -> int:
        s.replace(" ","")
        stack = []
        res , num , sign =  0 , 0 , 1
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "+" or ch == "-":
                res += num * sign
                num = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res , num , sign =  0 , 0 , 1
            elif ch == ")":
                res += sign * num
                num = 0 ; sign = 1
                res*= stack.pop()
                res += stack.pop()
        res += sign * num
        return res
                
        