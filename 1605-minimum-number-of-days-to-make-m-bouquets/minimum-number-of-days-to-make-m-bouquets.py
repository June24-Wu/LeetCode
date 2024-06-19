class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isValid(day):
            bouquets = 0
            adjacentNum = 0
            for i in bloomDay:
                if i <= day:
                    adjacentNum += 1
                    if adjacentNum == k:
                        bouquets += 1
                        adjacentNum = 0
                else:
                    adjacentNum = 0
            return bouquets >= m
        
        left = min(bloomDay) ; right = max(bloomDay)
        
        if not isValid(right):
            return -1
        while left < right:
            mid = (left+right) // 2
            if isValid(mid):
                right = mid
            else:
                left = mid + 1
        return right
                        
                    
        