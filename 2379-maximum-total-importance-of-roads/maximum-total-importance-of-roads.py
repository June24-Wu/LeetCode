class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = collections.defaultdict(int)
        for u, v in roads:
            count[u] += 1
            count[v] += 1
        count = [[v,k] for k , v in count.items()]
        count.sort(reverse = True) ; ans = 0
        for i in range(len(count)):
            ans += (n - i) * count[i][0]
        return ans
        