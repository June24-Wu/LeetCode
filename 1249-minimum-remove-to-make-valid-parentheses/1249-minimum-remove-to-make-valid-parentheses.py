class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = [] # (parentheses : index)
        for index , item in enumerate(s):
            if item == "(":
                stack.append(index)
            if item == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(index)
        newS = []
        for index in range(len(s)):
            if index not in stack:
                newS.append(s[index])
        return "".join(newS)
        