class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        return_li = []
        
        def backtracking(start_index):
            if start_index == length:
                return_li.append(nums[:])
                return
            for i in range(start_index,length):
                # if i > start_index and nums[i] == nums[i-1]:
                #     continue
                nums[i] , nums[start_index] = nums[start_index] , nums[i]
                backtracking(start_index+1)
                nums[i] , nums[start_index] = nums[start_index] , nums[i]
            return
        backtracking(0)
        
        l2 = []
        for i in return_li:
            i = str(i)
            i = i.replace("[","")
            i = i.replace("]","")
            l2.append(i)
        l2 = list(set(l2))
        l3 = []
        for i in l2:
            l3.append(i.split(","))
        return l3
        