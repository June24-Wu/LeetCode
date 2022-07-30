class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        total_diff = 0
        for i in range(1,len(nums)):
            pre = nums[i-1] ; curr = nums[i]
            diff = curr - pre - 1
            if total_diff + diff >= k:
                return pre + k - total_diff
            else:
                total_diff += diff
        return nums[-1] + k - total_diff
            
            
        