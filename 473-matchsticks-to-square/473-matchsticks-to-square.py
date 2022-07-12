class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(key = lambda x : - x)
        if len(matchsticks) < 4 or sum(matchsticks) % 4 != 0 or max(matchsticks) > sum(matchsticks) // 4:
            return False
        length = sum(matchsticks) // 4
        @lru_cache
        def dfs(index,buckets):
            if index == len(matchsticks):
                if max(buckets) == 0:
                    return True
                return False
            buckets = list(buckets)
            size = matchsticks[index]
            flag = False
            for idx in range(len(buckets)):
                if flag == True:
                    break
                if size <= buckets[idx]:
                    buckets[idx] -= size
                    flag = flag or dfs(index + 1,tuple(buckets))
                    buckets[idx] += size
            return flag
        return dfs(0,tuple([length] * 4))