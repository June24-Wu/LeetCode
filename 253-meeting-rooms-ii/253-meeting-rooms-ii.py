class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        maxTime = max([i[1] for i in intervals])
        dp  = [0 for _ in range(maxTime+1)]
        for i , j in intervals:
            dp[i] += 1
            dp[j] -= 1
        ans = 0
        room = 0 
        for i in dp:
            room += i
            ans = max(ans,room)
        return ans