class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                ten += 1
                five -= 1
                if five < 0:
                    return False
            else:  # i == 20
                twenty += 1
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
                
                if ten < 0 or five < 0: return False
        return True
                    

                
        