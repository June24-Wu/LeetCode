class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        ans = [events[0]]
        for i in range(1,len(events)):
            ans.append([events[i][0],events[i][1] - events[i-1][1]])
        ans.sort(key = lambda x : (- x[1],x[0]))
        # print(ans)
        return ans[0][0]
        