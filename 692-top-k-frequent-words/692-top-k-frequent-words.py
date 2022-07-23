class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        table = {}
        for i in words:
            if i not in table:
                table[i] = 0 
            table[i] += 1
        pq = []
        for i in table:
            heapq.heappush(pq,(-table[i],i))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(pq)[1])
        return ans
        