from typing import List

class Solution:
    def maxWeight(self, p: List[int]) -> int:
        p.sort()  # \U0001f522 Sort the pizzas in ascending order \U0001f355
        n = len(p)
        m = n // 4  # \U0001f4c6 Total number of days (each day we eat 4 pizzas)
        odd = (m + 1) // 2  # \U0001f535 Number of odd days
        even = m - odd  # \U0001f7e2 Number of even days
        
        total_weight = 0
        l = n - 1  # \U0001f519 l points to the last element
        
        # \U0001f535 On odd days, we gain the weight of the heaviest pizza in the set of 4
        for _ in range(odd):
            total_weight += p[l]  # \U0001f355 Pick the largest pizza
            l -= 1  # ⬅ Move left
        
        # \U0001f7e2 On even days, we gain the weight of the second heaviest pizza in the set of 4
        for _ in range(even):
            l -= 1  # ⏩ Skip third largest pizza
            total_weight += p[l]  # \U0001f355 Gain the weight of the second largest pizza
            l -= 1  # ⬅ Move left again
        
        return total_weight  # \U0001f522 Return maximum weight gained \U0001f3af