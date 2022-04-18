class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        def cntDays(treshold):
            day = 0 
            p1 = 0; p2 = 0
            weight = 0
            for i in weights:
                weight += i
                if weight > treshold:
                    day += 1
                    weight = i
            return day + 1
        left = max(weights) ; right = sum(weights)
        
        while left < right:
            mid = (left+right) // 2
            if cntDays(mid) == days:
                right = mid
            elif cntDays(mid) > days:
                left = mid + 1
            else:
                right = mid
        return right
            