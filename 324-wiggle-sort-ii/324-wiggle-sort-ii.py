class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = sorted(nums)
        n = len(nums2)
        if n % 2 == 0:
            arr1 = nums2[:n//2]
            arr2 = nums2[n//2:]
        else:
            arr1 = nums2[:n//2+1]
            arr2 = nums2[n//2+1:]
        for i in range(len(nums)):
            if i % 2== 0:
                nums[i] = arr1.pop()
            else:
                nums[i] = arr2.pop()
        return nums
        