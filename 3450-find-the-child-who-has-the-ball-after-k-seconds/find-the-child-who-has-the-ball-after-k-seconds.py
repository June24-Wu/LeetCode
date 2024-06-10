class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        curr = 0
        d = 1
        for _ in range(k):
            if 0 < curr < n-1:
                curr += d
            else:
                if curr == n-1:
                    d = -1
                    curr += d
                else:
                    d = 1
                    curr += d
        return curr
        