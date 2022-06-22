class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        left = [0 for _ in range(len(s))] ; right = [0 for _ in range(len(s))]
        cnt = 0
        for i in range(len(s)):
            left[i] = cnt
            if s[i] == "1":
                cnt += 1
        cnt = 0
        for i in range(len(s)-1,-1,-1):
            right[i] = cnt
            if s[i] == "0":
                cnt += 1
        
        ans = min(s.count("0"),s.count("1"))
        
        for index , item in enumerate(s):
            if item == "0":
                ans = min(ans,left[index] + right[index] + 1)
            else:
                ans = min(ans,left[index] + right[index])
        return ans
        