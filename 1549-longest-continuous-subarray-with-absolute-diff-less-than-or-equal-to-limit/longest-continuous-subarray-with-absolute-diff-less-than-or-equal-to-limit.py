class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0 ; min_h = [] ; max_h = []

        def clean():
            nonlocal min_h ; nonlocal max_h ; nonlocal left
            while min_h[0][1] < left:
                heapq.heappop(min_h)
            while max_h[0][1] < left:
                heapq.heappop(max_h)
            return
        ans = 0
        for right in range(len(nums)):
            heapq.heappush(min_h,[nums[right],right])
            heapq.heappush(max_h,[ - nums[right],right])
            clean()
            while min_h and max_h and - max_h[0][0] - min_h[0][0] > limit:
                left += 1
                clean()
            ans = max(ans,right-left + 1)
        return ans

                



        