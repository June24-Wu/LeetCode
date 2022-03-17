class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        return_li = []
        def backtracking(start_index):
            if start_index == length:
                return_li.append(nums[:])
                return
            for i in range(start_index,length):
                nums[i] , nums[start_index] = nums[start_index] , nums[i]
                backtracking(start_index+1)
                nums[i] , nums[start_index] = nums[start_index] , nums[i]
        backtracking(0)
        return return_li
        