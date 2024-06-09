class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in s:
            if i.isdigit():
                stack.pop() if stack else None
            else:
                stack.append(i)
        return "".join(stack)
            
        