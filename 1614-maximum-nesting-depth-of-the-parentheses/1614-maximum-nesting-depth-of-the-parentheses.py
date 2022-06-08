class Solution:
    def maxDepth(self, s: str) -> int:
        num = 0 ; cnt = 0
        for i in s:
            if i == "(":
                num += 1
            if i == ")":
                num -= 1
            else:
                cnt = max(cnt,num)
        return cnt
        