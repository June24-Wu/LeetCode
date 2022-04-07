class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        left , right = 0 , len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                i  , j = mid , mid
                while nums[i-1] == target and i >= 1:
                    i -= 1
                while j < len(nums) - 1 and nums[j+1] == target:
                    j += 1
                return [i,j]
            elif nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1,-1]