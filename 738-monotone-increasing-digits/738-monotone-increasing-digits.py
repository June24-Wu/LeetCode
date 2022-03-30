class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if len(str(n)) <= 1:return n
        n = list(str(n))
        
        for i in range(len(n)-1,0,-1):
            if int(n[i]) < int(n[i-1]):
                n[i-1] = str(int(n[i-1]) - 1)
                n[i:] = "9" * (len(n) - i)
        return int("".join(n))
        