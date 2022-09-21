class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, target: int) -> int:
        table = set()
        minute = target // 60
        second = target % 60
        
        def get(m,s):
            m = str(m) ; s = str(s)
            if m == "0":
                return s
            else:
                return m + s.zfill(2)
        char = get(minute,second)
        if len(char) <= 4:
            table.add(char)
        if second <= 39 and minute > 0:
            minute -= 1
            second += 60
            char = get(minute,second)
            if len(char) <= 4:
                table.add(char)
        startAt = str(startAt)
        ans = float("inf")
        # print(table)
        for time in table:
            curr = startAt
            cnt = 0
            for char in time:
                if curr == char:
                    cnt += pushCost
                else:
                    cnt += moveCost + pushCost
                    curr = char
            ans = min(cnt,ans)
        return ans
        # 