class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        
        for i in arr:
            heapq.heappush(heap,(abs(i-x),i))
        ans = []
        for _ in range(k):
            _ , val = heapq.heappop(heap)
            ans.append(val)
        ans.sort()
        return ans
        