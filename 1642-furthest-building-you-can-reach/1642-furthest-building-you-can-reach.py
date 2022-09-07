class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            height = heights[i + 1]  - heights[i]
            if height <= 0 :
                continue
            heapq.heappush(heap,height)
            if len(heap) <= ladders:
                continue
            bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1
        