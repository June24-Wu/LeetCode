class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        cal = 0 ; ans = 0
        for i in range(k):
            cal += calories[i]
        
        
        def calculate():
            nonlocal ans
            if cal > upper:
                ans += 1
            if cal < lower:
                ans -= 1
        calculate()
        for i in range(k,len(calories)):
            cal -= calories[i-k]
            cal += calories[i]
            calculate()
        return ans
            
        