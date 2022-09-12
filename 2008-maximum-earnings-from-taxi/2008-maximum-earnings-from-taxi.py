class Solution:
    def maxTaxiEarnings(self, n, rides):
        ans = sorted([(start, end, end - start + tip) for start, end, tip in rides])

        total, max_val, stack = 0, 0, []

        for s, e, income in ans:
            while stack and stack[0][0] <= s:
                total = max(total, heappop(stack)[1])

            heappush(stack, (e, total + income))
            max_val = max(max_val, total + income)

        return max_val
            
        