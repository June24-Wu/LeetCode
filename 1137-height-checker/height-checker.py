class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a  = sorted(heights)
        ans = 0
        for i in range(len(a)):
            if heights[i] != a[i]:
                ans += 1
        return ans
        