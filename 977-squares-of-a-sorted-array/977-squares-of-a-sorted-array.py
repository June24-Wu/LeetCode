class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # new = []
        # for i in nums:
        #     new.append(i*i)
        # new.sort()
        # return new
        new = [None for _ in range(len(nums))]
        left = 0
        right = len(nums) - 1
        p = len(new) - 1
        while p>=0:
            if nums[left] ** 2 < nums[right] ** 2:
                new[p] = nums[right] ** 2
                right -= 1
            else:
                new[p] = nums[left] ** 2
                left += 1
            p -= 1
        return new
        