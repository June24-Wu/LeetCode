class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                val = 0
                while True:
                    last = stack.pop()
                    if last == 0:
                        break
                    else:
                        val += last
                val = 1 if val == 0 else val * 2
                stack.append(val)
            # print(stack)
        return sum(stack)
            
        