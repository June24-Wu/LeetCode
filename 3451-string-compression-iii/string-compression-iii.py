class Solution:
    def compressedString(self, word: str) -> str:
        stack = []
        ans = ""
        for i in word:
            if not stack or (stack[-1] == i and len(stack) < 9):
                stack.append(i)
            else:
                ans += str(len(stack)) + stack[-1]
                stack = [i]
        if stack:
            ans += str(len(stack)) + stack[-1]
        return ans 
        