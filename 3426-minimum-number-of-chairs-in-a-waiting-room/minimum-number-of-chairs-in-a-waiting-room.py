class Solution:
    def minimumChairs(self, s: str) -> int:
        a = 0 ; ans = 0
        for i in s:
            if i == "E":
                a += 1
            else:
                a -= 1
            ans = max(a,ans)
        return ans


        