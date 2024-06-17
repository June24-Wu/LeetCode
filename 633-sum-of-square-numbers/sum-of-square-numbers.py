class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s = set()
        for i in range(int((2**31 - 1)**0.5 + 100)):
            if i ** 2 > c:
                break
            else:
                s.add(i**2)
        for i in s:
            if c - i in s:
                return True
        return False
        