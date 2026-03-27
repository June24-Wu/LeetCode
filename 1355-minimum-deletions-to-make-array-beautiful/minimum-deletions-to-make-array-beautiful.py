class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ans = 0
        m = len(nums)
        for idx in range(m - 1):
            new_idx = idx - ans
            # print(nums[idx],nums[idx+1],idx,new_idx)
            if new_idx % 2 == 0 and nums[idx] == nums[idx + 1]:
                ans += 1
        if (m - ans) % 2 != 0:
            ans += 1
        return ans


        