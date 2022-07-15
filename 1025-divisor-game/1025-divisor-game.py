class Solution:
    def divisorGame(self, n: int) -> bool:
        table = {1:False}
        
        for i in range(1,n+1):
            flag = False
            for j in range(i-1,0,-1):
                if i % j == 0:
                    flag = flag or not table[i-j]
            table[i] = flag
        return table[n]
        