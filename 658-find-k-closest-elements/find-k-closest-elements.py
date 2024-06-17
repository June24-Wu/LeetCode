class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []
        for idx , item in enumerate(arr):
            heapq.heappush(h,(abs(item-x),item))
        ans = []
        for _ in range(k) :
            _ , a = heapq.heappop(h)
            ans.append(a)
        return sorted(ans)
        