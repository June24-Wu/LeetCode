class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0 ; n = len(hours)
        for i in range(n):
            hours[i] = hours[i] % 24
        cnt = collections.defaultdict(int)
        for i in hours:
            if i != 0:
                ans += cnt[24 - i]
            else:
                ans += cnt[i]
            cnt[i] += 1
        return ans
        