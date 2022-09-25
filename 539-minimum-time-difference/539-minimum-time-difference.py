class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        li = []
        for i in timePoints:
            hour , minute = i.split(":")
            time = int(hour) * 60 + int(minute)
            li.append(time)
            li.append(time+60*24)
        li.sort()
        minval = float("inf")
        for i in range(1,len(li)):
            minval = min(minval,li[i] - li[i-1])
        return minval
        