class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first =  - heapq.heappop(stones)
            second = - heapq.heappop(stones)
            if first == second:
                continue
            remain = abs(first - second)
            heapq.heappush(stones,-remain)
        if stones != []:
            return - stones[0]
        return 0
        