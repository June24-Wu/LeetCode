class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        left_max = 0; right_max = 0
        for i in range(n):
            left_max = max(left_max,height[i])
            left[i] = left_max
        for i in range(n-1,-1,-1):
            right_max = max(right_max,height[i])
            right[i] = right_max
        ans = 0
        for i in range(n):
            ans += max(min(left[i],right[i]) - height[i],0)
        return ans

        