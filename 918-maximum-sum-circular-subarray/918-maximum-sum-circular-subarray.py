class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s = sum(nums)
        if len(nums) == 1:
            return s
        def kadane(array):
            curr = 0 ; ans = 0
            for i in array:
                curr = max(curr + i , 0)
                ans = max(curr,ans)
            if ans == 0:
                return max(array)
            return ans
        ans1 = kadane(nums)
        ans2 = s + kadane([- nums[i] for i in range(len(nums) - 1)])
        ans3 = s + kadane([- nums[i] for i in range(1 , len(nums))])
        return max(ans1,ans2,ans3)