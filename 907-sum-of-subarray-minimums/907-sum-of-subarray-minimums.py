class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        
        arr.append(0)
        mod = 10**9 + 7
        ans = 0
        stack = [-1]
        for idx2 , item in enumerate(arr):
            while stack and item < arr[stack[-1]]:
                mid = stack.pop()
                left = mid - stack[-1]
                right = idx2 - mid
                ans += left * right * arr[mid]
            stack.append(idx2)
        return ans % mod
                