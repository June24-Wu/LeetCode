class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        table = []
        for s , e in intervals:
            table.append((s,1))
            table.append((e,-1))
        table.append((toBeRemoved[0],-1))
        table.append((toBeRemoved[1],1))
        flag = False ; cnt = 0 ; ans = []
        table.sort()
        # print(table)
        for idx , val in table:
            cnt += val
            if cnt >= 1 and not flag:
                s = idx
                flag = True
            if cnt < 1 and flag and idx - s >= 1:
                ans.append([s,idx])
                flag = False
        return ans

        