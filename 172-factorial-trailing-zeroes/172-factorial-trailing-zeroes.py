class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 1 
        for i in range(n,0,-1):
            num *= i
        num = str(num)
        count = 0
        for i in range(len(num)-1,-1,-1):
            if num[i] != "0":
                break
            count += 1
        return count
        