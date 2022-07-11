class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() ; ans = set()
        for idx , first in enumerate(nums):
            target = - first
            left = idx + 1 ; right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    ans.add((first,nums[left],nums[right]))
                    right -= 1
        return list(ans)
                    
        