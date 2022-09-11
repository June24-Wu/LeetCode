class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        candidates = zip(efficiency, speed)
        candidates = sorted(candidates, key=lambda t:t[0], reverse=True)
        print(candidates)
        speed_heap = []
        speed_sum, perf = 0, 0
        for curr_efficiency, curr_speed in candidates:
            if len(speed_heap) > k-1:
                speed_sum -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, curr_speed)
            speed_sum += curr_speed
            perf = max(perf, speed_sum * curr_efficiency)
        return perf % (10**9 + 7)
        