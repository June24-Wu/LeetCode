class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        arr = [0 for _ in range(len(piles))]
        def count(i):
            for j in range(len(piles)):
                arr[j] = piles[j] // i + 1 if piles[j] % i != 0 else piles[j] // i
            # print(arr)
            return sum(arr)
        
        left , right = 1, max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            if count(mid) <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left
        