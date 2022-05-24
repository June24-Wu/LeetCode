class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        newList = []
        for i in intervals:
            newList.append((i[0],1))
            newList.append((i[1],-1))
        newList.sort(key = lambda x : (x[0],x[1]))
        curr = 0
        ans = 0
        for time , status in newList:
            if status == 1:
                curr += 1
                ans = max(ans,curr)
            else:
                curr -= 1
        return ans
        
        
        
        
        
        
        
        
        
        
        #1 
        # maxTime = max([i[1] for i in intervals])
        # dp  = [0 for _ in range(maxTime+1)]
        # for i , j in intervals:
        #     dp[i] += 1
        #     dp[j] -= 1
        # ans = 0
        # room = 0 
        # for i in dp:
        #     room += i
        #     ans = max(ans,room)
        # return ans