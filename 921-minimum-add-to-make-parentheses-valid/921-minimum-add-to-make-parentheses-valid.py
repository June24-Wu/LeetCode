class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        num = 0 ; cnt = 0
        
        for i in s:
            if i == "(":
                num += 1
            else:
                if num > 0:
                    num -= 1
                else:
                    cnt += 1
        return cnt + num
        