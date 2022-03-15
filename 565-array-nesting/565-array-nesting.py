class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        return_val = 0
        for i in range(len(nums)):
            cnt = 0
            p = i
            while nums[p] != -1:
                print(p)
                cnt += 1
                index = nums[p]
                nums[p] = -1
                p = index
            return_val = max(return_val,cnt)
            print("=========")
        return return_val
        