class Solution:
    def candy(self, ratings: List[int]) -> int:
        heap = []
        for idx , rate in enumerate(ratings):
            heap.append((rate,idx))
        heapq.heapify(heap)
        dp = [1 for _ in range(len(ratings))]
        while heap:
            rating , idx = heapq.heappop(heap)
            candy = 1
            if idx - 1 >= 0 and ratings[idx] > ratings[idx - 1]:
                candy = max(candy,dp[idx - 1] + 1)
            if idx + 1 < len(ratings) and ratings[idx] > ratings[idx + 1]:
                candy = max(candy,dp[idx + 1] + 1)  
            dp[idx] = candy
        return sum(dp)