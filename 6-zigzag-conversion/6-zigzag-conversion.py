class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        heap = []
        k = 0 ; p = 0 
        while p < len(s):
            if k == 0:
                for i in range(numRows):
                    if p < len(s):
                        heapq.heappush(heap,(i,p,s[p]))
                        p += 1
                    else:
                        break
                k = numRows - 2
            else:
                heapq.heappush(heap,(k,p,s[p]))
                p += 1
                k -= 1
        row = 0
        ans = []
        temp = []
        while heap:
            temp = []
            while heap and heap[0][0] == row:
                temp.append(heapq.heappop(heap)[2])
            row += 1
            ans.append("".join(temp))
        return "".join(ans)
                
        