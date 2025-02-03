class Solution:
    def maxFreeTime(self, eventTime: int, cnt: int, startTime: List[int], endTime: List[int]) -> int:
        time = [[i,j] for i , j in zip(startTime,endTime)]
        time.sort()
        free = []
        free.append(time[0][0])
        for k in range(1,len(startTime)):
            free.append(time[k][0] - time[k-1][1])
        free.append(eventTime - time[-1][1])
        ans = 0; curr = 0
        print(free)
        for i in range(cnt+1):
            curr += free[i]
        ans = curr
        for i in range(cnt+1,len(free)):
            curr -= free[i-cnt-1]
            curr += free[i]
            ans = max(curr,ans)
            print(curr,ans)
        return ans

        