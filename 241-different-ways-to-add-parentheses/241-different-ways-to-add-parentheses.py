class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        if expression.isdigit():
            return [int(expression)]
        
        for index, char in enumerate(expression):
            if char in ["+","-","*"]:
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])
                # print(left)
                for l in left:
                    for r in right:
                        if char == "+":
                            res.append(l+r)
                        if char == "-":
                            res.append(l-r)
                        if char == "*":
                            res.append(l*r)
        return res