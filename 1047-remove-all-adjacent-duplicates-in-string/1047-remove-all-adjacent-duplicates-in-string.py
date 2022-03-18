class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack == []:
                stack.append(i)
            else:
                a = stack.pop()
                if a == i:
                    continue
                else:
                    stack.append(a)
                    stack.append(i)
        return "".join(stack)
        