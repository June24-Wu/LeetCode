class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ""
        num = ""
        for i in s:
            if i.isdigit():
                num += i
            elif i == "[":
                stack.append(num)
                num = ""
                stack.append(i)
            elif i == "]":
                char = ""
                while stack[-1] != "[":
                    char = stack.pop() + char
                stack.pop()
                cnt = int(stack.pop())
                char = cnt * char
                stack.append(char)
            else:
                stack.append(i)
        for i in stack:
            ans += i
        return ans
        