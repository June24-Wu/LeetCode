class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total = len(nums) - 1
        i = 0
        while i < total:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                total -= 1
            else:
                i += 1
        return None
                
        