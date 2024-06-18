class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort(reverse = True)
        h = [(-i,j) for i,j in zip(profit,difficulty)]
        heapq.heapify(h) ; ans = 0
        for i in worker:
            while h and i < h[0][1]:
                heapq.heappop(h)
                # print(h)
            # print(h,ans)
            ans -= h[0][0] if h else 0
        return ans

        