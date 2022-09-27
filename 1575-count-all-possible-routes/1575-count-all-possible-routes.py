class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        table = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i== j:
                    continue
                table[i].append((abs(locations[i] - locations[j]),j))
            table[i].sort()
        mod = 10**9 + 7 
        @cache
        def dfs(index,curr_fuel):
            if curr_fuel < 0:
                return 0
            if curr_fuel == 0:
                return index == finish
            ans = 0
            if index == finish:
                ans += 1
            for cost , des in  table[index]:
                if cost > curr_fuel:
                    break
                ans = (ans + dfs(des,curr_fuel - cost)) % mod
            return ans % mod
        return dfs(start,fuel) % mod
            
        