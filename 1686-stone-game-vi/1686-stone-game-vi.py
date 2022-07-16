class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        arr = []
        for i in range(len(aliceValues)):
            arr.append((aliceValues[i] + bobValues[i],i))
        arr.sort()
        x = 0 ; y = 0
        for cnt, (_ , i) in enumerate(arr[::-1]):
            if cnt % 2 == 0:
                x += aliceValues[i]
            else:
                y += bobValues[i]
        if x > y :
            return 1
        if x < y:
            return  - 1
        return 0
        
            
