class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        def dfs():
            stack  = []
            while s:
                char = s.pop(0)
                if char == "(":
                    stack += dfs()
                elif char == ")":
                    return stack[::-1]
                else:
                    stack.append(char)
            return stack
        return "".join(dfs())
        