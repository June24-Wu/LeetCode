class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        def calculator(s:list):
            num = 0 ; sign = "+" ; stack = []
            while s:
                item = s.popleft()
                if item.isdigit():
                    num = num* 10 + int(item)
                if item == "(":
                    num = calculator(s)
                if not item.isdigit() or len(s) == 0:
                    if sign == "+":
                        stack.append(num)
                    if sign == "-":
                        stack.append(-num)
                    if sign == "*":
                        stack.append(stack.pop() * num)
                    if sign == "/":
                        stack.append(int(stack.pop() / float(num)))
                    sign = item
                    num = 0
                if item == ")": break
            return sum(stack)
        return calculator(collections.deque(s))
                    
