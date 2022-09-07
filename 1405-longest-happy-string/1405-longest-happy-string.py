class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        
        
        for cnt , char in [(a,"a"),(b,"b"),(c,"c")]:
            if cnt != 0:
                heapq.heappush(heap,(-cnt,char))
        ans = "" ; samecnt = 1
        while heap:
            cnt , char = heapq.heappop(heap)
            if len(ans) > 1 and char == ans[-1] and char == ans[-2]:
                if heap:
                    cnt1 , char1 = heapq.heappop(heap)
                    cnt1 = - cnt1
                    ans += char1
                    if cnt1 - 1 != 0:
                        heapq.heappush(heap,(-(cnt1 - 1) , char1))
                else:
                    break
            ans += char
            cnt = - cnt
            if cnt -1 != 0:
                heapq.heappush(heap,(-(cnt - 1) , char))
        return ans
        