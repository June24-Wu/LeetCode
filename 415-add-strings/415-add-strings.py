class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        def get(index,num):
            if 0 <= index < len(num):
                return int(num[index])
            return 0
        
        p1 = len(num1) - 1
        p2 = len(num2) - 1 

        final = 0
        add = 0
        final = ""
        while p1 >= 0 or p2 >= 0:
            first = get(p1,num1)
            second = get(p2,num2)
            leftVal = (first + second + add) % 10
            add = (first + second + add) // 10
            final = str(leftVal) + final
            p1 -= 1 ; p2 -= 1
        if add != 0:
            final = str(add) + final 
        return final

            
        