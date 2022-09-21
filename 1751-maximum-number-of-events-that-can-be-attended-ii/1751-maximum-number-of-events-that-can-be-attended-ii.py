class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        startTime = [events[i][0] for i in range(len(events))]
        n = len(events)
        events.sort()
        startTime.sort()
        print(events)
        @lru_cache
        def dfs(index,cnt):
            if index == n or cnt == k:
                return 0
            next = bisect_left(startTime,events[index][1]+1)
            return max(dfs(index+1,cnt),events[index][2] + dfs(next,cnt+1))
        return dfs(0,0)
        