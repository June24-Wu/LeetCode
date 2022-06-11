class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        # two pass
        cntl = 0 ; cntr = 0 ; ans = 0
        for i in range(len(s)):
            if s[i] == "(":
                cntl += 1
            else:
                cntr += 1
            if cntl == cntr:
                ans = max(ans,2*cntl)
            if cntr > cntl:
                cntr = cntl = 0
        cntl = 0 ; cntr = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "(":
                cntl += 1
            else:
                cntr += 1
            if cntl == cntr:
                ans = max(ans,2*cntl)
            if cntr < cntl:
                cntr = cntl = 0        
        return ans