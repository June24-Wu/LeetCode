class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            if i  in [")","]","}"]:
                if stack == []:
                    return False 
                value = stack.pop()
                if i == ")" and value != "(":
                    return False
                if i == "]" and value != "[":
                    return False
                if i == "}" and value != "{":
                    return False
        return stack == []
        