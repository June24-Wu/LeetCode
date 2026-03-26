class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x : x[0])

        prices = [None for _ in range(len(items))]
        max_num = [None for _ in range(len(items))]

        curr = 0
        for i in range(len(items)):
            prices[i] = items[i][0]
            curr = max(items[i][1],curr)
            max_num[i] = curr
        # print(items)
        # print(prices)
        # print(max_num)

        ans = []
        for q in queries:
            idx = bisect_right(prices,q) - 1
            ans.append(max_num[idx]) if idx >= 0 else ans.append(0)
        return ans
        