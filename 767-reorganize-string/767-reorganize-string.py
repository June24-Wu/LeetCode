class Solution:
    def reorganizeString(self, s: str) -> str:
        table = Counter(s)
        heap = [(-table[i],i) for i in table]
        heapq.heapify(heap)
        ans = ""
        while heap:
            cnt , char = heapq.heappop(heap)
            if len(ans) == 0 or ans[-1] != char:
                ans += char
                if cnt +1 != 0:
                    heapq.heappush(heap,(cnt+1,char))
            else:
                if not heap:
                    return ""
                cnt2 , char2 = heapq.heappop(heap)
                ans += char2
                if cnt2+1 != 0:
                    heapq.heappush(heap,(cnt2+1,char2))
                heapq.heappush(heap,(cnt,char))
        return ans
                
        