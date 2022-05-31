class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack , num , sign = [], 0 , "+"
        for index , ch in enumerate(s):
            if ch.isdigit():
                num = num*10 + int(ch)
            if index == len(s) - 1 or not ch.isdigit():
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                elif sign == "/":
                    if stack[-1] > 0:
                        stack.append(stack.pop()//num)
                    else:
                        stack.append(int(stack.pop()/num))
                sign = ch
                num = 0
        ans = 0
        for i in stack:
            ans += i
        return ans