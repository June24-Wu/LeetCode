class Solution:
    def isHappy(self, n: int) -> bool:
        table = set()
        
        
        while n not in table:
            table.add(n)
            val = 0
            for i in str(n):
                val += int(i) **2
            if n == 1:
                return True
            n = val
        return False
        