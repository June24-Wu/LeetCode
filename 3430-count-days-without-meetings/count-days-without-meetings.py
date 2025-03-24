class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        left = meetings[0][0]
        right = meetings[0][1]
        ans = left - 1
        # print(ans)
        for l , r in meetings[1:]:
            if l <= right:
                right = max(r,right)
            else:
                ans += l - right - 1
                left = l ; right = r
        return ans + days - right
        