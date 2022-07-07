class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def __rob(array):
            if len(array) == 1:
                return array[0]
            array[1] = max(array[0],array[1])
            for i in range(2,len(array)):
                array[i] = max(array[i - 1] , array[i] + array[i - 2])
            return array[-1]
        return max(__rob(nums[:-1]), __rob(nums[1:]))
        