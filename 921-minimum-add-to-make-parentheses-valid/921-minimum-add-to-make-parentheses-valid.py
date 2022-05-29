class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        
        for i in s:
            if i == "(":
                # if stack and stack[-1] == ")":
                #     stack.pop()
                # else:
                    stack.append(i)
            if i == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)
        