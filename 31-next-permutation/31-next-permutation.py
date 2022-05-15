class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        origin = nums.copy()
        for i in range(length-2,-1,-1):
            if nums[i] >= nums[i+1]:
                continue
            else:
                for j in range(length-1,i,-1):
                    if nums[j] > nums[i]:
                        nums[j] , nums[i] = nums[i] , nums[j]
                        break
                    else:
                        continue
                subArray = nums[i+1:].copy()
                subArray = subArray[::-1]
                nums[i+1:] = subArray
                return nums
        nums.sort()
        return nums
                