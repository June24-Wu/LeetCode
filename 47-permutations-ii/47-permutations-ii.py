class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        length = len(nums)
        def backtracking(start_index):
            if start_index == length:
                ans.append(tuple(nums[:]))
                return
            for i in range(start_index,length):
                nums[i] , nums[start_index] = nums[start_index] , nums[i]
                backtracking(start_index+1)
                nums[i] , nums[start_index] = nums[start_index] , nums[i]
            return
        backtracking(0)
        ans = list(set(ans))
        return [list(i) for i in ans]
        