class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        curr = 1 ; d = -1
        for _ in range(time):
            if 1 < curr < n:
                curr += d
            else:
                d = 1 if d == -1 else -1
                curr += d
            # print(curr)
        return curr


        