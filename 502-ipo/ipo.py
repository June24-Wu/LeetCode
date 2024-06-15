class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        h = [(j, -i) for i , j in zip(profits,capital)]
        heapq.heapify(h)
        heap = []
        for _ in range(k):
            while h and w >= h[0][0]:
                c , p = heapq.heappop(h)
                heapq.heappush(heap,(p))
            if heap:
                p = heapq.heappop(heap)
                w -= p
            else:
                break
        return w

            
        