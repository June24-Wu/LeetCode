class Solution:
    def findMin(self, nums: List[int]) -> int:
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         return nums[i+1]
        # return nums[0]
        left = 0 ; right = len(nums) - 1
        
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]