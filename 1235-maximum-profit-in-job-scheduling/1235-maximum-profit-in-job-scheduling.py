class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = list(zip(startTime,endTime,profit))
        jobs.sort()
        startTime.sort()
        @lru_cache
        def dfs(index):
            if index == n:
                return 0
            next = bisect_left(startTime,jobs[index][1])
            return max(dfs(next) + jobs[index][2],dfs(index+1))
        return dfs(0)
            